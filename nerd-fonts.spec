%global fontname nerd

Name:           %{fontname}-fonts
Version:        2.1.0
Release:        1%{?dist}
Summary:        Nerd Fonts patched with a high number of glyphs

License:        OFL
URL:            https://github.com/ryanoasis/nerd-fonts
Source1:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraCode.zip
Source2:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/SourceCodePro.zip
Source3:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.zip
Source4:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/DejaVuSansMono.zip
Source5:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/UbuntuMono.zip
Source6:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/DroidSansMono.zip


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


%package -n nerd-jetbrains-mono-fonts
Summary: Monospaced font family for user interface and coding environments

Requires:       fontpackages-filesystem

%description -n nerd-jetbrains-mono-fonts
Patched font JetBrains Mono from nerd-fonts library.


%package -n nerd-ubuntu-mono-fonts
Summary: Monospaced font family for user interface and coding environments

Requires:       fontpackages-filesystem

%description -n nerd-ubuntu-mono-fonts
Patched font Ubuntu Mono from nerd-fonts library.


%package -n nerd-droid-sans-mono-fonts
Summary: Monospaced font family for user interface and coding environments

Requires:       fontpackages-filesystem

%description -n nerd-droid-sans-mono-fonts
Patched font Droid Sans Mono from nerd-fonts library.


%package -n nerd-dejavu-sans-mono-fonts
Summary: Monospaced font family for user interface and coding environments

Requires:       fontpackages-filesystem

%description -n nerd-dejavu-sans-mono-fonts
Patched font DejaVu Sans Mono from nerd-fonts library.



%prep
rm -rf %{_builddir}/%{name}-%{version}/*
unzip %{SOURCE1} -d %{_builddir}/%{name}-%{version}
unzip %{SOURCE2} -d %{_builddir}/%{name}-%{version}
unzip %{SOURCE3} -d %{_builddir}/%{name}-%{version}
unzip %{SOURCE4} -d %{_builddir}/%{name}-%{version}
unzip %{SOURCE5} -d %{_builddir}/%{name}-%{version}
unzip %{SOURCE6} -d %{_builddir}/%{name}-%{version}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/F[iu]ra*Code*.otf %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/Sauce*Code*Pro*.ttf %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/JetBrains*Mono*.ttf %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/Ubuntu*Mono*.ttf %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/Droid*Sans*Mono*.otf %{buildroot}%{_fontdir}

install -m 0644 -p %{_builddir}/%{name}-%{version}/DejaVu*Sans*Mono*.ttf %{buildroot}%{_fontdir}

# Remove unused fonts
find %{buildroot} -name "*Windows*Compatible.ttf" -delete

%files -n nerd-fira-code-fonts
%{_fontdir}/Fira*Code*.otf
%{_fontdir}/Fura*Code*.otf


%files -n nerd-source-code-pro-fonts
%{_fontdir}/Sauce*Code*Pro*.ttf

%files -n nerd-jetbrains-mono-fonts
%{_fontdir}/JetBrains*Mono*.ttf

%files -n nerd-ubuntu-mono-fonts
%{_fontdir}/Ubuntu*Mono*.ttf

%files -n nerd-droid-sans-mono-fonts
%{_fontdir}/Droid*Sans*Mono*.otf

%files -n nerd-dejavu-sans-mono-fonts
%{_fontdir}/DejaVu*Sans*Mono*.ttf


%changelog
* Thu July 21 2022 Serhii Tsynailo <serhii.tsynailo@gmail.com> - 2.1.0-1
- Initial package provides nerd Fira Code, Source Code Pro, JetBrains, Ubunt, Droid and DejaVu mono fonts
