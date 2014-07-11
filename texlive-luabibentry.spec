# revision 31783
# category Package
# catalog-ctan /macros/luatex/latex/luabibentry
# catalog-date 2013-09-27 07:27:17 +0200
# catalog-license lppl1.3
# catalog-version 0.1a
Name:		texlive-luabibentry
Version:	0.1a
Release:	7
Summary:	Repeat BibTeX entries in a LuaLaTeX document body
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luabibentry
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package reimplements bibentry, for use in LuaLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
