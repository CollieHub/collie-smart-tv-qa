# Guía de Emuladores para QA - Collie Smart TV

Para testear la aplicación sin hardware físico, utilizaremos los emuladores oficiales. Esta guía detalla cómo configurar cada uno.

## 1. Samsung Tizen (Opción Recomendada)
Samsung ofrece el simulador más completo para probar la lógica de red.

### Instalación:
1.  Descarga **Tizen Studio** con el **Integrated SDK** desde [Samsung Developers](https://developer.samsung.com/smarttv/viewing/tools-and-tools/tizen-studio/download.html).
2.  Abre el **Package Manager**.
3.  Instala:
    *   `Tizen SDK Tools` -> `Baseline SDK`
    *   `Tizen SDK Tools` -> `Extension SDK` -> `TV Extensions`
    *   `Tizen SDK Tools` -> `Emulator`

### Uso:
1.  Lanza el **Emulator Manager**.
2.  Crea un nuevo VM de tipo **TV** (ej: `tv-7.0-x86`).
3.  Inícialo. El emulador tendrá su propia IP en tu red local (puenteada) y la App de Collie lo detectará como una TV real.

---

## 2. LG webOS Simulator 
LG utiliza una aplicación de escritorio muy liviana.

### Instalación:
1.  Descarga el **webOS TV Simulator** desde [LG webOS TV Developer](https://webostv.developer.lge.com/develop/tools/tv-simulator).
2.  Instálalo en tu Mac.

### Uso:
1.  Abre el Simulator.
2.  Verás que tiene botones integrados para simular la IP y el estado de la red.
3.  Asegúrate de que el puerto **3000** esté abierto en tu firewall de macOS para que la App pueda verlo.

---

## 3. Android TV (AVD)
Ideal para probar dispositivos Sensei, TCL y el driver de Google Cast.

### Configuración:
1.  Abre **Android Studio**.
2.  Ve a **Device Manager**.
3.  **Create Device** -> Categoría **TV** -> Selecciona **Android TV (1080p)**.
4.  Selecciona una imagen de sistema (preferentemente API 30+).
5.  **IMPORTANTE:** En la configuración del AVD, asegúrate de que el **Network** esté en modo `Bridged` (si es posible) para que aparezca en la misma red que tu celular físico.

---

## 4. Collie Mock Server (Python)
Para pruebas rápidas de interfaz y envío de comandos.

### Uso:
1.  Navega a `mocks/tv-server/`.
2.  Ejecuta: `python3 samsung_mock.py`.
3.  Abre la App Collie en tu celular (conectado al mismo WiFi que la Mac).
4.  La App debería detectar "Collie Mock TV" automáticamente.
