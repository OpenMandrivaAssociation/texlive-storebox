Name:		texlive-storebox
Version:	64967
Release:	2
Summary:	Storing information for reuse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/storebox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides "store boxes" whose user interface matches
that of normal LaTeX "save boxes", except that the content of a
store box appears at most once in the output PDF file, however
often it is used. The present version of the package supports
pdfLaTeX and LuaLaTeX; when DVI is output, store boxes behave
the same as save boxes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/storebox/storebox-pgf.sty
%{_texmfdistdir}/tex/latex/storebox/storebox.sty
%doc %{_texmfdistdir}/doc/latex/storebox/README
%doc %{_texmfdistdir}/doc/latex/storebox/storebox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/storebox/storebox.dtx
%doc %{_texmfdistdir}/source/latex/storebox/storebox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
