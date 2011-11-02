Name:		texlive-lcyw
Version:	v1.1
Release:	1
Summary:	Make Classic Cyrillic CM fonts accessible in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lcyw
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package makes the classic CM Cyrillic fonts accessible for
use with LaTeX.

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
%{_texmfdistdir}/tex/latex/lcyw/cmap-cyr-vf.sty
%{_texmfdistdir}/tex/latex/lcyw/koi7a.cmap
%{_texmfdistdir}/tex/latex/lcyw/lcywcmr.fd
%{_texmfdistdir}/tex/latex/lcyw/lcywcmss.fd
%{_texmfdistdir}/tex/latex/lcyw/lcywcmssq.fd
%{_texmfdistdir}/tex/latex/lcyw/lcywcmtt.fd
%{_texmfdistdir}/tex/latex/lcyw/lcywenc.def
%doc %{_texmfdistdir}/doc/latex/lcyw/README
%doc %{_texmfdistdir}/doc/latex/lcyw/README.koi8-r
%doc %{_texmfdistdir}/doc/latex/lcyw/example-lcyw.tex
%doc %{_texmfdistdir}/doc/latex/lcyw/lcyw.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lcyw/lcyw.dtx
%doc %{_texmfdistdir}/source/latex/lcyw/lcyw.ins
%doc %{_texmfdistdir}/source/latex/lcyw/lcywfd.fdd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
