%global tl_name pmhanguljamo
%global tl_revision 78114

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Poor mans Hangul Jamo input method
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/korean/pmhanguljamo
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmhanguljamo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmhanguljamo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Hangul transliteration input method that allows
to typeset Korean letters (Hangul) using the proper fonts. The name is
derived from "Poor man's Hangul Jamo Input Method". The use of XeLaTeX
is recommended. pdfTeX is not supported.

