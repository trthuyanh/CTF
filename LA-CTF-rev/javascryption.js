    const s5 = atob("JTNEJTNEUWZsSlglNUJPTERfREFUQSU1RG85MWNzeFdZMzlWZXNwbmVwSjMlNUJPTERfREFUQSU1RGY5bWI3JTVCT0xEX0RBVEElNURHZGpGR2I=")
    const s4 = decodeURIComponent(s5)
    const s3 = s4.replaceAll("[OLD_DATA]", "Z");
    const s2 = s3.split("").reverse().join("");
    const s1 = atob(s2)
    alert(s1)
