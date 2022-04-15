# Qtile

![Arch](https://user-images.githubusercontent.com/103541228/163500834-82d4f907-cfc8-4c39-bd31-89538018cf26.png)

# Índice 
- [Instalación de Qtile](#instalación-de-qtile)
- [Genera las carpetas de usuario](#genera-las-carpetas-de-usuario)
- [Instala un Aur helper](#instala-un-aur-helper)
- [Instala un navegador](#instala-un-navegador)
- [Fuente necesaria](#fuente-necesaria)
- [Utiliza mis configuraciones](#utiliza-mis-configuraciones)
- [Cambia la Shell por defecto](#cambia-la-shell-por-defecto)
- [Archivo xprofile](#archivo-xprofile)
- [Habilita la sintaxis de color en nano](#habilita-la-sintaxis-de-color-en-nano)
- [Temas](#temas)
- [Utiliza lxappearance](#utiliza-lxappearance)
- [Cambia el fondo de pantalla](#cambia-el-fondo-de-pantalla)
- [Problemas de screen tearing](#problemas-de-screen-tearing)
- [Función de cada programa que utilizo](#función-de-cada-programa-que-utilizo)
- [Atajos de teclado (Keybindings) de mi configuración](#atajos-de-teclado-de-mi-configuración)

# Instalación de Qtile y Programas necesarios

Instala Qtile, X11, LightDM y un emulador de terminal:

```bash
sudo pacman -S xorg xorg-xinit xorg-server lightdm lightdm-gtk-greeter qtile alacritty fish nemo cinnamon-translations nemo-fileroller rofi nitrogen scrot redshift file-roller gvfs glib2 gvfs-mtp udiskie network-manager-applet pulseaudio pavucontrol pamixer alsa-utils brightnessctl playerctl gedit eog arandr picom xdg-user-dirs ntfs-3g lxappearance vlc dunst nano light neovim
```
Habilita LightDM:

```bash
sudo systemctl enable ligthdm
```
En este punto, puedes reiniciar tu equipo y entrar en Qtile, o bien, continuar desde la línea de comandos.

# Genera las carpetas de usuario

Con el siguiente comando se generarán las carpetas comúnes de usuario: Descargas, Imágenes, Documentos...

```bash
xdg-user-dirs-update
```

# Instala un Aur helper

Programas necesarios:

```bash
sudo pacman -S git base-devel
```
Clona el repositorio de Yay/Paru

En Arch Linux y sus derivadas, podemos utilizar un "Aur Helper", para facilitar la instalación de paquetes "AUR". Aquí te dejo 2 "Aur Helpers", puedes utilizar uno o ambos:

Yay:

```bash
git clone https://aur.archlinux.org/yay-git.git
```

Paru:

```bash
git clone https://aur.archlinux.org/paru-git.git
```

Instala Yay/Paru como aur helper:

```bash
cd yay-git/ 
makepkg -si
```

```bash
cd paru-git/ 
makepkg -si
```
# Instala un navegador

Este es mi navegador de uso diario, brave:

Con Yay:

```bash
yay -S brave-bin
```

Con Paru:

```bash
paru -S brave-bin
```

# Fuente necesaria

Si no instalamos esta fuente, las letras y widgets de mi configuración, no se podrán ver correctamente:

Yay:

```bash
yay -S nerd-fonts-ubuntu-mono
```

Paru:

```bash
paru -S nerd-fonts-ubuntu-mono
```

Debes reiniciar la sesión para que el sistema cargue las fuentes. Puedes continuar y reiniciar luego, o reiniciar en este momento:

```bash
kill -9 -1
```

# Utiliza mis configuraciones

Clona mi repositorio

```bash
git clone https://github.com/dilxxn/dotfiles.git
```

Opcional: Clona mi repositorio de Wallpapers.

```bash
git clone https://github.com/dilxxn/wallpapers.git
```

Mueve las carpetas a sus lugares:

```bash
cp -r dotfiles/.config ~/
cp -r dotfiles/.local ~/
cp dotfiles/.xprofile ~/
cp -r Wallpapers/ ~/Imágenes
```

Remplaza "(user)" por tu nombre de usuario con la herramienta "Buscar y remplazar" de gedit en su menú:

```bash
gedit ~/.config/qtile/settings/keys.py
```

Puedes presionar Super (Tecla Windows) + Control + R para recargar la configuración de Qtile.

Estos wallpapers fueron obtenidos desde el repositorio del YouTube "DistroTube"

Su canal de YouTube:
https://www.youtube.com/c/DistroTube

Su GitLab:
https://gitlab.com/dwt1

# Cambia la Shell por defecto

En mi caso, utilizo fish como shell por defecto:

```bash
sudo usermod --shell /usr/bin/fish user
sudo usermod --shell /usr/bin/fish root
```

# Archivo xprofile

El archivo .xprofile, aloja los comandos que se ejecutan al iniciar la sesión, este archivo debe ubicarse en la carpeta "/home/(usuario)/" puedes revisarlo y agregar más comandos si lo deseas:

```bash
nano ~/.xprofile
```

# Habilita la sintaxis de color en nano
Por defecto, nano nos mostrará siempre un texto plano, por lo que si queremos tener colores, debemos hacer lo siguiente:

sudo nano /etc/nanorc

Busca utilizando ctrl + w la línea # include "/usr/share/nano/*.nanorc" y descomentala.

# Temas

--- Fondo de pantalla ---

Utilizando el programa "Nitrogen", podrás cambiar los fondos de pantalla que utilices, sin embargo, si presionas Super (Tecla Windows) + W, podrás cambiar aleatoriamente entre los fondos de pantalla que hayas agregado en Nitrogen.

--- Tema de Qtile ---

Presiona Super + Alt + (Números entre 1 - 5)

--- Tema de LightDM: ---

```bash
sudo pacman -S lightdm-webkit2-greeter
```

Paru:

```bash
paru -S lightdm-webkit-theme-aether
```

Yay:

```bash
yay -S lightdm-webkit-theme-aether
```

Pudes cambiar la configuración desde el siguiente archivo:

```bash
sudo nano /etc/lightdm/lightdm-webkit2-greeter.conf
```

En mi caso, he cambiado el tema por "antergos", puedes hacerlo modificando la línea de "webkit_theme":

```bash
webkit_theme = antergos
```

--- Tema de Fish shell ---

```bash
sudo pacman -S fisher
fisher install IlanCosman/tide@v5
```

--- Tema de NeoVim ---

Si prefieres utilizar NeoVim, aquí tienes mi configuración de este:

```bash
cd
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
nvim +'hi NormalFloat guibg=#1e222a' +PackerSync
```

--- Tema de GRUB: ---

Descarga el tema "Vimix" para GRUB:

https://www.gnome-look.org/p/1009236/

Suponiendo que estás en la carpeta donde se encuentra el tema de GRUB, ejecuta los siguientes comandos:

Puedes cambiar "Vimix-1080p.tar.xz" por las variantes que hay (Vimix-4k.tar.xz) | (Vimix-2k.tar.xz).

```bash
tar xvf Vimix-1080p.tar.xz
cd Vimix-1080p
sudo bash install.sh
```

--- Tema GTK: ---

Este es el tema GTK que utilizo, escoge los que más de gusten:

https://www.gnome-look.org/p/1357889/

--- Tema de íconos: ---

Aquí puedes descargar el tema de íconos que utilizo, puedes escoger los que más te gusten.

https://www.gnome-look.org/p/1279924/

# Utiliza lxappearance

Este programa nos permitirá cambiar entre los temas GTK que hayamos descargado. Estos temas se deben alojar en las carpetas ~/.themes & ~/.icons.

Puedes abrirlo utilizando Tecla Super + M y buscando lxappearance.

# Cambia el fondo de pantalla

Utiliza el programa Nitrogen para cambiar el fondo de pantalla, puedes lanzarlo presionando Super (Tecla windows) + m y buscando "nitrogen".

Presiona "Preferencias" y agrega la ubicación de tus Wallpapers, si utilizaste mis configuraciones, estarán en la carpeta Imágenes.

# Problemas de screen tearing

Si tienes problemas como screen tearing, modificar el siguiente archivo puede ayudarte:

```bash
sudo nano /etc/xdg/picom.conf
```

Busca utilizando Ctrl + W y comenta la línea <<backend = "xrender";>> y descomenta la línea <<"backend = "glx">>:

# Función de cada programa que utilizo

| Programa               | Función                               |
| ---------------------- | ------------------------------------- |
| Alacritty              | Emulador de terminal                  |
| fish                    | Shell con mejoras sobre bash          |
| rofi                    | Menú de aplicaciones                  |
| nitrogen               | Administrar fondos de pantalla        |
| scrot                  | Captura de pantalla                   |
| redshift               | Luz noctura                           |
| gvfs & glib2           | Papelera de reciclaje                 |
| udiskie                | Administra Unidades de almacenamiento |
| network-manager-applet | Administrador de redes                |
| pulseaudio             | Soporte para audio                    |
| pamixer                | Control del sonido por terminal       |
| alsa-utils             | Utilidades de sonido extra            |
| brightnessctl          | Soporte para control de brillo        |
| playerctl              | Control de audio multimedia           |
| nano                   | Editor de texto para terminal         |
| gedit                  | Editor de texto gráfico                |
| arandr                 | Configuración de pantallas gráfico      |
| picom                  | Compositor de ventanas para xorg      |
| geeqie                 | Visualizar imágenes                   |
| xdg-user-dirs          | Crea los directorios comúnes          |
| ntfs-3g                | Permite lectura de discos NTFS        |
| lxappearance           | Administra temas GTK                  |
| vlc                    | Visualizar videos                     |

# Atajos de teclado de mi configuración

La tecla "mod" es la tecla Windows, o más conocida como tecla Super en Linux.

| Atajo de teclado       | Función                               |
| ---------------------- | ------------------------------------- |
| mod + q                | Cerrar la ventana enfocada            |
| mod + w                | Selecciona un fondo aleatorio         |
| mod + t                | Selecciona un tema para Qtile         |
| mod + enter            | Abrir alacritty                       |
| mod + m                | Abrir rofi                             |
| mod + b                | Abrir brave                           |
| mod + r                | Activa luz noctura (redshift)         |
| mod + shift + r        | Desactiva luz noctura                 |
| mod + s                | Captura de toda la pantalla           |
| mod + shift s          | Captura de área a seleccionar         |
| ---------------------- | ------------------------------------- |
