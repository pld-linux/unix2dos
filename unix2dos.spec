Summary:	unix2dos - UNIX to DOS text file format converter
Summary(fr.UTF-8):	Convertisseur de format de fichier texte
Summary(pl.UTF-8):	unix2dos - konwerter plików tekstowych z formatu UNIX na DOS
Summary(pt_BR.UTF-8):	Conversor de formatos de arquivos texto
Summary(ru.UTF-8):	unix2dos - конвертор текстовых файлов UNIX в формат DOS
Summary(uk.UTF-8):	unix2dos - конвертор текстових файлів UNIX в формат DOS
Name:		unix2dos
Version:	2.2
Release:	22
License:	BSD-like
Group:		Applications/Text
Source0:	%{name}-%{version}.src.tar.gz
# Source0-md5:	e4488c241fa9067a48a7534a21d4babb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in UNIX format to DOS format.

%description -l fr.UTF-8
unix2dos converti des fichier texte UNIX au format DOS.

%description -l pl.UTF-8
Zestaw narzędzi do konwersji plików tekstowych w formacie UNIX na
format używany przez DOS-a.

%description -l pt_BR.UTF-8
O unix2dos converte arquivos texto do UNIX para o formato texto do
DOS.

%description -l ru.UTF-8
unix2dos - конвертор текстовых файлов UNIX в формат DOS.

%description -l uk.UTF-8
unix2dos - конвертор текстових файлів UNIX в формат DOS.

%prep
%setup -q -c

%build
%{__cc} %{rpmcflags} -o unix2dos unix2dos.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install unix2dos $RPM_BUILD_ROOT%{_bindir}
install unix2dos.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
