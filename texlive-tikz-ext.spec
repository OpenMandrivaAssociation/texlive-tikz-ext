Name:		texlive-tikz-ext
Version:	66737
Release:	1
Summary:	A collection of libraries for PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-ext
License:	fdl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-ext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-ext.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a collection of libraries for PGF/TikZ. Currently these
are transformations.mirror, paths.arcto, paths.ortho,
paths.timer, patterns.images, topaths.arcthrough and misc. Most
of these libraries were developed in response to questions on
TeX.stackexchange.com.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/tikz-ext
%{_texmfdistdir}/tex/latex/tikz-ext
%{_texmfdistdir}/tex/generic/tikz-ext
%doc %{_texmfdistdir}/doc/latex/tikz-ext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
