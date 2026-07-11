%global tl_name storebox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3a
Release:	%{tl_revision}.1
Summary:	Storing information for reuse
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/storebox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides "store boxes" whose user interface matches that of
normal LaTeX "save boxes", except that the content of a store box
appears at most once in the output PDF file, however often it is used.
The present version of the package supports pdfLaTeX and LuaLaTeX; when
DVI is output, store boxes behave the same as save boxes.

