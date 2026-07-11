%global tl_name luabibentry
%global tl_revision 55777

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1a
Release:	%{tl_revision}.1
Summary:	Repeat BibTeX entries in a LuaLaTeX document body
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luabibentry
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luabibentry.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package reimplements bibentry, for use in LuaLaTeX.

