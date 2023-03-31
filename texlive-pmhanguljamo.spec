Name:		texlive-pmhanguljamo
Version:	64361
Release:	2
Summary:	Poor man's Hangul Jamo input method
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pmhanguljamo
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmhanguljamo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmhanguljamo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a Hangul transliteration input method
that allows to typeset Korean letters (Hangul) using the proper
fonts. The name is derived from "Poor man's Hangul Jamo Input
Method". The use of XeLaTeX is recommended. pdfTeX is not
supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pmhanguljamo
%doc %{_texmfdistdir}/doc/latex/pmhanguljamo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
