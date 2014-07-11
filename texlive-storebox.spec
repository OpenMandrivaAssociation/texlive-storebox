# revision 24895
# category Package
# catalog-ctan /macros/latex/contrib/storebox
# catalog-date 2011-12-21 11:26:33 +0100
# catalog-license lppl1.3
# catalog-version 1.3a
Name:		texlive-storebox
Version:	1.3a
Release:	8
Summary:	Storing information for reuse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/storebox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storebox.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3a-2
+ Revision: 756251
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3a-1
+ Revision: 745329
- texlive-storebox

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719592
- texlive-storebox
- texlive-storebox
- texlive-storebox
- texlive-storebox

