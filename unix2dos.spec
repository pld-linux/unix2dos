Summary:	unix2dos - UNIX to DOS text file format converter
Summary(fr):	Convertisseur de format de fichier texte
Summary(pl):	unix2dos - konwerter plik�w tekstowych z formatu UNIX na DOS
Summary(pt_BR):	Conversor de formatos de arquivos texto
Summary(ru):	unix2dos - ��������� ��������� ������ UNIX � ������ DOS
Summary(uk):	unix2dos - ��������� ��������� ���̦� UNIX � ������ DOS
Name:		unix2dos
Version:	2.2
Release:	3
License:	BSD-like
Group:		Applications/Text
Source0:	%{name}-%{version}.src.tar.gz
# Source0-md5:	e4488c241fa9067a48a7534a21d4babb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in UNIX format to DOS format.

%description -l fr
unix2dos converti des fichier texte UNIX au format DOS.

%description -l pl
Zestaw narz�dzi do konwersji plik�w tekstowych w formacie UNIX na
format u�ywany przez DOS-a.

%description -l pt_BR
O unix2dos converte arquivos texto do UNIX para o formato texto do
DOS.

%description -l ru
unix2dos - ��������� ��������� ������ UNIX � ������ DOS.

%description -l uk
unix2dos - ��������� ��������� ���̦� UNIX � ������ DOS.

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
