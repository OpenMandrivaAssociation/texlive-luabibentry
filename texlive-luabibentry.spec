# revision 23435
# category Package
# catalog-ctan /macros/luatex/latex/luabibentry
# catalog-date 2011-06-30 18:17:02 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-luabibentry
Version:	0.1
Release:	1
Summary:	Repeat BibTeX entries in a LuaLaTeX document body
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luabibentry
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package reimplements bibentry, for use in LuaLaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/luabibentry/luabibentry.lua
%{_texmfdistdir}/tex/lualatex/luabibentry/luabibentry.sty
%doc %{_texmfdistdir}/doc/lualatex/luabibentry/News
%doc %{_texmfdistdir}/doc/lualatex/luabibentry/README
%doc %{_texmfdistdir}/doc/lualatex/luabibentry/luabibentry.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/luabibentry/Makefile
%doc %{_texmfdistdir}/source/lualatex/luabibentry/luabibentry.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
