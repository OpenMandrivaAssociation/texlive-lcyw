%global tl_name lcyw
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Make Classic Cyrillic CM fonts accessible in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lcyw
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes the classic CM Cyrillic fonts accessible for use with
LaTeX.

