%global fontname nerd

Name:           %{fontname}-fonts
Version:        2.1.0
Release:        1%{?dist}
Summary:        Nerd Fonts patched with a high number of glyphs

License:        OFL
URL:            https://github.com/ryanoasis/nerd-fonts
Source1:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraCode.zip
Source2:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/SourceCodePro.zip

BuildArch:      noarch
BuildRequires:  fontpackages-devel
# BuildRequires:  libappstream-glib
BuildRequires:  unzip

Requires:       fontpackages-filesystem

%description
Nerd Fonts patches developer targeted fonts with a high number of glyphs
(icons). Specifically to add a high number of extra glyphs from popular ‘iconic
fonts’ such as Font Awesome, Devicons, Octicons, and others.


%package -n nerd-fira-code-fonts
Summary: Free monospaced font with programming ligatures

Requires:       fontpackages-filesystem

%description -n nerd-fira-code-fonts
Patched font Fira (Fura) Code from the nerd-fonts library.


%package -n nerd-source-code-pro-fonts
Summary: Monospaced font family for user interface and coding environments

Requires:       fontpackages-filesystem

%description -n nerd-source-code-pro-fonts
Patched font SourceCodePro from nerd-fonts library.


%prep
rm -rf %{_builddir}/%{name}-%{version}/*
unzip %{SOURCE1} -d %{_builddir}/%{name}-%{version}
unzip %{SOURCE2} -d %{_builddir}/%{name}-%{version}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/F[iu]ra*Code*.otf %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/Sauce*Code*Pro*.ttf %{buildroot}%{_fontdir}


%files -n nerd-fira-code-fonts
%{_fontdir}/Fira*Code*.otf
%{_fontdir}/Fura*Code*.otf


%files -n nerd-source-code-pro-fonts
%{_fontdir}/Sauce*Code*Pro*.ttf


%changelog
* Sun May 08 2022 Serhii Tsynailo <serhii.tsynailo@gmail.com> - 2.1.0-1
- Initial package provides nurd Fira Code and Source Code Pro
