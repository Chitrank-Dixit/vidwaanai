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

### Verse 1 (Markende Puran 0.881)
- **Original**: (अ0 22। 27-- 34)
- **Translation**: 

---

### Verse 2 (Markende Puran 0.882)
- **Original**: मै माह त मे स्वख्रा प्राप्ता प्रोतिनूपेद्रशों। श्रुल्णा सुनिपरित्राणे हर्त पुत्र यथा मयां
- **Translation**: 

---

### Verse 3 (Markende Puran 0.883)
- **Original**: शॉचता बान्धवानों मे निश्वरन्तो्ातेद:गखित्ता:। प्रियन्ते व्याधिना क्लिष्टास्तेषां सातां छुृधाप्रजा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.884)
- **Original**: प्ग्रागा युध्यव्राना य्रेड्भोता गोड्िजरक्षणे। छ्ुण्णप. शस्त्रैर्विपधस्तें त॑ एड भुत्रि मानवा;
- **Translation**: 

---

### Verse 5 (Markende Puran 0.885)
- **Original**: अर्थिनां मित्रवर्गस्थ वांद्रपाँ च पराइमुझत। यो ते याति पिता तेन पुत्री पाता थे बीरसू:
- **Translation**: 

---

### Verse 6 (Markende Puran 0.886)
- **Original**: गर्भक्लेश; स्त्रियों मत्ये साफल्‍ृ्दं भजते तटा! झद्दारिविजयी 7 स्यातू संग्राम वा इतः सुतः
- **Translation**: 

---

### Verse 7 (Markende Puran 0.887)
- **Original**: (अ0 22। 46-75)
- **Translation**: 

---

### Verse 8 (Markende Puran 0.888)
- **Original**: ज्र संक्षिप्त मार्कण्डेय पुराण* हब 0753404677004 60840 6 210 06600 7744007 64707 66.27 46620 *632:00 का 20270 # 4 तदन-्तर य्रज शतरुजितते अपनी पुत्रवधू मदालपाक्ा हर्ष छा रहा है। पिता माता तथा अन्य बन्धु- दाह-संस्कार किया और गगरसे बाहर निकलकर पुत्रको
- **Translation**: 

---

### Verse 9 (Markende Puran 0.889)
- **Original**: थान्थबोंने उन्हें छातीसे लगाया और “निरंगौबी जलाअलि दी। तालकेतु फिर यमुनाजलसे निकलकर
- **Translation**: 

---

### Verse 10 (Markende Puran 0.890)
- **Original**: रहो वत्स!' यह कहकर कल्याणमय आशीर्वाद दिया। राजकुमारके पास गया और प्रेमपूर्वक मीठी बाणीपें राजकुमार भी सबको प्रणाम ऋरके आश्चर्यमग्न बोज्ला-' राजकुमार! अब तुप जाओ। तुपने मुझे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.891)
- **Original**: हो पूछने लगे--'यह क्या बात हैं?' पितासे कृतार्थ कर दिया। तुम जो यहाँ अतिचह्न भावसे खड़े पूछनेघर उन्होंने बीती हुई स्रारी बातें कढ़ रहें, इससे मैंने बहुत दिवोंकों अपनी अभिलाषा पूरी
- **Translation**: 

---

### Verse 12 (Markende Puran 0.892)
- **Original**: सुदायों
- **Translation**: 

---

### Verse 13 (Markende Puran 0.893)
- **Original**: अपनी मनोस्मा भार्या मदालसाको पृत्युका कर लो। मुज्े मा कप कि ल्यि
- **Translation**: 

---

### Verse 14 (Markende Puran 0.894)
- **Original**: समाचार सुनकर हार कक पित्ताको सामने चारझण यहका अनुछझव करनेकी बहुत दिनोंते अभिलाषा
- **Translation**: 

---

### Verse 15 (Markende Puran 0.895)
- **Original**: खड़ा देख वे लजा और शोकके समुद्गमें डूब थी; वह सब कार्य अब मैंने पूरा कर लिया।' उसके
- **Translation**: 

---

### Verse 16 (Markende Puran 0.896)
- **Original**: एय्ने और मन-हों-मन सोचने लगै--' हाय! उस यों कहनेपर राजकुमार उसको प्रणप कस्के गझड़ ' साध्वी बालाने मेरी मृत्युकौ बात सुनकर प्राण तथा वायुके समान जेगवाले उसो अश्वपर आड़ हुए
- **Translation**: 

---

### Verse 17 (Markende Puran 0.897)
- **Original**: त्याग दिये; फिर भी मैं जोवित हूँ। मुझ निह्ठुरकों औए अपने पिताके नगरकी ओर चल दिये। घिल्‍कार है। अहो! मैं क्रूर हूँ, अनाय॑ हूँ, जो मेरे राजकुमार ऋ्ध्वज बड़े बेगसे अपने नगरमें
- **Translation**: 

---

### Verse 18 (Markende Puran 0.898)
- **Original**: हो लिये मृत्युकों प्राप्त हुई उस मृगनयनी पत्नोके आये। उस समय उनके मनमें भातता-पिताके । बिना भो अत्यन्त निर्दय होकर जी रहा हूँ।' इसके अरणोंकी उन्दता करने तथा मदालसाको देखदेकी
- **Translation**: 

---

### Verse 19 (Markende Puran 0.899)
- **Original**: जाद उन्होंने अपने मनके आवेशको रोच्छा और प्रबल इच्छा थो। वहाँ पहुँचकर उन्होंने देखा, सामने
- **Translation**: 

---

### Verse 20 (Markende Puran 0.900)
- **Original**: मोह छोड़कर विचारता आरम्भ क्विया--'' वह मर आनेवाले प्रभी लोग उद्धिग्न हैं, किसौंके मुखपर
- **Translation**: 

---

