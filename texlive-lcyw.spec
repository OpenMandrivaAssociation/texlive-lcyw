# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/lcyw
# catalog-date 2009-12-16 19:51:33 +0100
# catalog-license lppl1.3
# catalog-version v1.1
Name:		texlive-lcyw
Version:	v1.1
Release:	10
Summary:	Make Classic Cyrillic CM fonts accessible in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lcyw
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcyw.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes the classic CM Cyrillic fonts accessible for
use with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.1-2
+ Revision: 753212
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.1-1
+ Revision: 718839
- texlive-lcyw
- texlive-lcyw
- texlive-lcyw
- texlive-lcyw

