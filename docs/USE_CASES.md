# Casos de Uso - Collie Smart TV

Este documento detalla los flujos críticos de la aplicación que deben ser validados mediante pruebas de QA.

## UC-001: Descubrimiento de Dispositivos (Discovery)
**Actor:** Usuario
**Descripción:** El usuario inicia la aplicación y busca televisores disponibles en su red local.
**Precondiciones:** El televisor y el dispositivo móvil están en la misma red Wi-Fi.
**Flujo Principal:**
1. El usuario abre la app.
2. La app inicia el escaneo automático (SSDP, mDNS).
3. Aparece una lista de dispositivos encontrados con su marca y modelo.
**Postcondiciones:** El usuario ve al menos un televisor disponible para conectar.

## UC-002: Control Remoto Básico
**Actor:** Usuario
**Descripción:** El usuario interactúa con los botones del control remoto virtual para manejar la TV.
**Precondiciones:** La app está conectada a un televisor.
**Flujo Principal:**
1. El usuario presiona el botón "Volume Up".
2. El televisor incrementa el volumen.
3. El usuario presiona "Mute".
4. El televisor silencia el audio.
**Postcondiciones:** Las comandos se ejecutan con latencia mínima.

## UC-003: Emparejamiento con PIN (Samsung/LG/Panasonic)
**Actor:** Usuario / Sistema
**Descripción:** Ciertas marcas requieren un código PIN para autorizar la conexión.
**Precondiciones:** El televisor soporta emparejamiento por PIN.
**Flujo Principal:**
1. El usuario intenta conectar a un televisor Samsung.
2. El televisor muestra un código de 4 u 8 dígitos en pantalla.
3. La aplicación muestra un diálogo solicitando el PIN.
4. El usuario ingresa el código y confirma.
**Postcondiciones:** La conexión se establece y el token se guarda de forma segura.

## UC-004: Modo Simulación (QA Hub)
**Actor:** Tester
**Descripción:** Validar el comportamiento de la UI sin tener una TV física.
**Precondiciones:** Servidor mock activo (`mocks/tv-server/`).
**Flujo Principal:**
1. El tester activa el modo simulación en la app.
2. El sistema detecta "Samsung Mock TV" y "LG Mock TV".
3. El tester envía comandos y verifica que el servidor mock reciba las peticiones correctamente.
**Postcondiciones:** Se verifican los flujos de UI de forma aislada.

---
© 2026 CollieTech
