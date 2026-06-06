# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Bramha 0.1441)
- **Original**: था। ये बोले-'हाय! ग्राहसे पकड़े जानेके कारण सुनकर भगवान्‌ शह्ूरने देवीके पास आकर
- **Translation**: 

---

### Verse 2 (Bramha 0.1442)
- **Original**: मैं अचेत हो रहा हूँ। कोई हो तो मुझे आकर कहा--' तुम्हारे पिताने स्वयंवर होनेकी बात कही
- **Translation**: 

---

### Verse 3 (Bramha 0.1443)
- **Original**: बचाये।' पीड़ित ब्राह्मणकी वह पुकार सुनकर है। उसमें तुम जिसका वरण करोगी, बही तुम्हारा
- **Translation**: 

---

### Verse 4 (Bramha 0.1444)
- **Original**: कल्याणमयी देवी पार्वती सहसा उठ खड़ी हुईं पति होगा। उस समय किसी रूपवान्‌कों छोड़कर
- **Translation**: 

---

### Verse 5 (Bramha 0.1445)
- **Original**: और उस स्थानपर गयीं, जहाँ वह ज्राह्मण-बालक तुम मुझ-जैसे अयोग्यका वरण कैसे करोगी?”
- **Translation**: 

---

### Verse 6 (Bramha 0.1446)
- **Original**: खड़ा था। बहाँ पहुँचकर चन्द्रमुखी देबीने देखा, उनके यों कहनेपर पार्वतीने उनकी बातोंपर
- **Translation**: 

---

### Verse 7 (Bramha 0.1447)
- **Original**: एक बहुत सुन्दर बालक ग्राहके मुखमें पड़ा धरथर विचार कखे हुए कहा-' महाभाग ! आपको अन्यथा
- **Translation**: 

---

### Verse 8 (Bramha 0.1448)
- **Original**: काँप रहा है। ग्राहके खींचनेपर वह तेजस्वी बालक विचार नहीं करना चाहिये। यैं आपका ही वरण
- **Translation**: 

---

### Verse 9 (Bramha 0.1449)
- **Original**: बड़ा आर्तनाद करता था। उस ग्राहग्रस्त यालकको करूँगी। इसमें कोई अनोखी बात नहीं है। अथवा
- **Translation**: 

---

### Verse 10 (Bramha 0.1450)
- **Original**: देखकर देवी उमा दुःखसे आतुर हो उ्ीं और यदि आपको मुझपर संदेह है तो मैं यहीं आपका
- **Translation**: 

---

### Verse 11 (Bramha 0.1451)
- **Original**: बोलीं--'ग्राहराज! यह अपने पिता-माताका बरण करती हूँ।' यों कहकर पार्वतीने अपने
- **Translation**: 

---

### Verse 12 (Bramha 0.1452)
- **Original**: ही बालक है, इसे शीघ्र छोड़ दो।' हाथोंसे अशोकका गुच्छा लेकर भगवान्‌ शब्टूरके
- **Translation**: 

---

### Verse 13 (Bramha 0.1453)
- **Original**: . ग्राहने कहा--देवि! छठे दिनपर जो सबसे कंधेपर रखा और कहा--देव! मैंने आपका
- **Translation**: 

---

### Verse 14 (Bramha 0.1454)
- **Original**: पहले मेरे पास आ जाता है, उसीको- विधाताने मेरा वरण कर लिया।' भगवती पार्वतीके इस प्रकार
- **Translation**: 

---

### Verse 15 (Bramha 0.1455)
- **Original**: आहार निश्चित किया है। महाभागे! यह बालक वरण करनेपर भगवान्‌ शड्भरने उस अशोक-
- **Translation**: 

---

### Verse 16 (Bramha 0.1456)
- **Original**: आज छठे दिन नयाजीसे प्रेरित होकर ही मेंरे पास वृक्षको अपनी वाणीसे सजीव करते हुए-से
- **Translation**: 

---

### Verse 17 (Bramha 0.1457)
- **Original**: आया है, अतः मैं इसे किसी प्रकार न छोड़ँगा। कहा--' अशोक! तुम्हारे परम पवित्र गुच्छेसे मेत
- **Translation**: 

---

### Verse 18 (Bramha 0.1458)
- **Original**: . देवी बोलीं--ग्राहराज ! मैंने हिमालयके शिखरपर बरण हुआ है, इसलिये तुम जरावस्थासे रहित एवं
- **Translation**: 

---

### Verse 19 (Bramha 0.1459)
- **Original**: जो उत्तम तपस्या की है, उसका पुण्य लेकर इस अमर रहोगे। तुम जैसा चाहोगे, वैसा रूप धारण
- **Translation**: 

---

### Verse 20 (Bramha 0.1460)
- **Original**: बालकको छोड़ दो। मैं तुम्हें नमस्कार करती हूँ। कर सकोगे। तुममें इच्छानुसार फूल लगेंगे। तुम
- **Translation**: 

---

