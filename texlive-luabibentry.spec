Name:		texlive-luabibentry
Version:	55777
Release:	1
Summary:	Repeat BibTeX entries in a LuaLaTeX document body
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luabibentry
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
