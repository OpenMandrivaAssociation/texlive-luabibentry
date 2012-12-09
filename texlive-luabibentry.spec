# revision 23435
# category Package
# catalog-ctan /macros/luatex/latex/luabibentry
# catalog-date 2011-06-30 18:17:02 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-luabibentry
Version:	0.1
Release:	2
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

%define		_unpackaged_subdirs_terminate_build	0

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 754350
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 718919
- texlive-luabibentry
- texlive-luabibentry
- texlive-luabibentry
- texlive-luabibentry

