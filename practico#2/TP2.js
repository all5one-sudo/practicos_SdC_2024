const ffi = require("ffi-napi");

// Carga la librería dinámica
const mylib = ffi.Library("./TP2_mac_arm.dylib", {
  process_data: ["int", ["float"]],
});

// Llama a la función 'process_data' definida en la librería
const result = mylib.process_data(3.7);
console.log("El resultado de process_data es:", result);
