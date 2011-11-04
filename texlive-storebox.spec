# revision 24355
# category Package
# catalog-ctan /macros/latex/contrib/storebox
# catalog-date 2011-10-21 09:17:17 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-storebox
Version:	1.1
Release:	1
Summary:	Storing information for reuse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/storebox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides "store boxes" whose user interface matches
that of normal LaTeX "save boxes", except that the content of a
store box appears at most once in the output PDF file, however
often it is used. The present version of the package supports
pdfLaTeX and LuaLaTeX; when DVI is output, store boxes behave
the same as save boxes.

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
%{_texmfdistdir}/tex/latex/storebox/storebox.sty
%doc %{_texmfdistdir}/doc/latex/storebox/README
%doc %{_texmfdistdir}/doc/latex/storebox/storebox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/storebox/storebox.dtx
%doc %{_texmfdistdir}/source/latex/storebox/storebox.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
