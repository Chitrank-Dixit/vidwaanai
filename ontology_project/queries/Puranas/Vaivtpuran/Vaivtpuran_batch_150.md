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

### Verse 1 (Vaivtpuran 10.9876)
- **Original**: वह स्वयं भी श्रीहरिके भारसे आक्रान्त हो वहाँ हुई थीं। उस समय गोकुलमें बवंडरका रूप
- **Translation**: 

---

### Verse 2 (Vaivtpuran 10.9877)
- **Original**: पृथ्वीपर गिर पड़ा। श्रीहरिका स्पर्श प्राप्त करके धारण करनेवाला तृणावर्त आ रहा था। मन-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 10.9878)
- **Original**: वह असुर भी भगवद्धामको चला गया। अपने ही-मन उसके आगमनकी बात जानकर श्रीहरिने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 10.9879)
- **Original**: कर्मोंका नाश करके सुन्दर दिव्य रथपर आरूढ़ अपने शरीरका भार बढ़ा लिया। उस भारसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 10.9880)
- **Original**: हो गोलोकमें जा पहुँचा। वह पाण्ड्यदेशका राजा पीड़ित होकर मैया यशोदाने लालाकों गोदसे उतार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 10.9881)
- **Original**: था और दुर्वासाके शापसे असुर हो गया था। दिया और खाटपर सुलाकर बे यमुनाजीके किनारे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 10.9882)
- **Original**: श्रीकृष्णके चरणोंका स्पर्श पाकर उसने गोलोकधाममें चली गयीं। इसी बीचमें वह बवंडररूपधारी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 10.9883)
- **Original**: स्थान प्राप्त कर लिया। असुर वहाँ आ पहुँचा और उस बालककों लेकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 10.9884)
- **Original**: मुने! बबंडरका रूप समाप्त होनेपर भयसे घुमाता हुआ सौ योजन ऊपर जा पहुँचा। उसने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 10.9885)
- **Original**: विह्ल गोप-गोपियोंने जब खोज की, तब बालकको वृक्षोंकी डालियाँ तोड़ दीं तथा इतनी धूल उड़ायी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 10.9886)
- **Original**: शय्यापर न देखकर सब लोग शोकसे व्याकुल हो *दत्त्वा विषस्तनं कृष्ण पूतना राक्षसी मुने । मुक्ति मातृगतिं प्राप कं भजामि बिना हरिम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 10.9887)
- **Original**: ( श्रीकृष्णजन्मखण्ड 10
- **Translation**: 

---

### Verse 13 (Vaivtpuran 10.9888)
- **Original**: # भ्रीकृष्णजन्मखण्ड * डड5 कक ऋऊऋऋऋकऋक कक ऋ# ऋ####ऋ########################ऋऊ$ऊऊऊककक55$%%% 54 #####%## भयसे अपनी-अपनी छाती पीटने लगे। कुछ लोग
- **Translation**: 

---

### Verse 14 (Vaivtpuran 10.9889)
- **Original**: इसी बीच अपने हजारों शिष्योंकों साथ लिये मूच्छित हो गये और कितने ही फूट-फूटकर रोने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 10.9890)
- **Original**: महामुनि दुर्वासा उधरसे निकले। मतवाले सहखाक्षने लगे। खोजते-खोजते उन्हें वह बालक ब्रजके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 10.9891)
- **Original**: उनकों देख लिया, पर वे न जलसे निकले, न भीतर एक फुलवाड़ीमें पड़ा दिखायी दिया।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 10.9892)
- **Original**: प्रणाम किया, न वाणीसे या हाथके संकेतसे ही उसके सारे अड्ग धूलसे धूसर हो रहे थे। एक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 10.9893)
- **Original**: कुछ कहा। इस चिर्लज्जञता और उदण्डताको सरोवरके बाहरी तटपर जो पानोसे भीगा हुआ था,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 10.9894)
- **Original**: देखकर दुर्वासाने उनको योगश्रष्ट होकर भारतमें पड़ा हुआ वह बालक आकाशकी ओर एकटक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 10.9895)
- **Original**: लाख वर्षोंतक असुरयोगिमें रहनेका शाप दे दिया देखता और भयसे कातर होकर बोलता था।
- **Translation**: 

---

