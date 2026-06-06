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

### Verse 1 (Rig Ved 0.361)
- **Original**: अत्यन्त सुखकारी रथ में नियोजित इन्धदेव के दोनों हरि (घोड़े) उन्हें (इद्धदेव को) घृत से स्निग्ध हवि रूप धाना (भुने हुए जौ) ग्रहण करने के लिए यहाँ ले आएँ
- **Translation**: 

---

### Verse 2 (Rig Ved 0.362)
- **Original**: 161. इन्द्र प्रातर्हववामह इन्द्रं प्रयत्यघ्वरे । इन्द्र सोमस्य पीतये
- **Translation**: 

---

### Verse 3 (Rig Ved 0.363)
- **Original**: हम प्रात:ःकाल यज्ञ प्रारम्भ करते समय मध्याह्कालीन सोमयाग प्रारम्भ होने पर तथा सायंकाल यज्ञ की समाप्ति पर भी सोमरस पीने के निमित्त इन्रदेव का आवाहन करते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.364)
- **Original**: 162. उ प नः सुतमा गहि हरिभिरिन्द्र केशिभिः। सुते हि त्वा हवामहे
- **Translation**: 

---

### Verse 5 (Rig Ved 0.365)
- **Original**: हे इन्धदेव ! आप अपने केसर युक्त अश्वों से सोम के अभिषव स्थान के पास आएँ । सोम के अभिषुत होने पर हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.366)
- **Original**: मं0 1 सू0 17 19 163. सेम॑ नः स्तोममा गद्मुपेदं सबन॑ सुतम्‌। गौरो न तृषित: पिब
- **Translation**: 

---

### Verse 7 (Rig Ved 0.367)
- **Original**: है इद्धदेव ! हमारे स्तोत्रों का श्रवण कर आप यहाँ आएँ । प्यासे गौर मृग के सदृश व्याकुल मन से सोम के अभिषव स्थान के समीप आकर सोम का पान करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.368)
- **Original**: 164. इमे सोमास इन्दव: सुतासो अधि ब्हिंषि। ता इन्द्र सहसे पिब
- **Translation**: 

---

### Verse 9 (Rig Ved 0.369)
- **Original**: हे इद्धदेव ! यह दीप्तिमान्‌ सोम निष्पादित होकर कुश-आसन पर सुशोभित है । शक्ति - वर्द्धन के निमित्त आप इसका पान करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.370)
- **Original**: 165, अबं ते स्तोमो अग्रियो हृदिस्पृगस्तु शंतम:। अथा सोम॑ सुतं पिय
- **Translation**: 

---

### Verse 11 (Rig Ved 0.371)
- **Original**: है इन्द्रदेव ! यह स्तोत्र श्रेष्ठ. मर्मस्प्शीं और अत्यन्त सुखकारी है। अब आप इसे सुनकर अभिषुत सोमरस का पान करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.372)
- **Original**: 166. विश्वमित्सवनं सुतमिन्द्रो मदाय गच्छति। चृत्रहा सोमपीतये
- **Translation**: 

---

### Verse 13 (Rig Ved 0.373)
- **Original**: । सोम के सभी अभिषव स्थानों की ओर इन्द्रदेव अवश्य जाते हैं । दुष्टों का हनन करने वाले इन्द्रदेव सोमरस पीकर अपना हर्ष बढ़ाते हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.374)
- **Original**: 167. सेम॑ न: काममा पृण गोभिरश्वै: शतक्रतो । स्तवाम त्वा स्वाध्य:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.375)
- **Original**: है शतकर्मा इन्द्रदेव ! आप हमारी गौओं और अश्यों सम्बन्धी कामनायें पूर्ण करें । हम मनोयोगपूर्वक आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.376)
- **Original**: सिक्त - 17 ] [ऋषि- मेधातिधि काण्व । देवता- इन्द्रावरण । छन्‍्द - गायत्री 4 पादनिचृत्‌ गायत्री, 5 हसीयसी गायत्री ] 168. इन्द्रावरुणयोरहं सम्राजोरव आ बृणे। ता नो मृत्ठात ईदशे
- **Translation**: 

---

### Verse 17 (Rig Ved 0.377)
- **Original**: हम इन्द्र और वरुण दोनों प्रतापी देवों से अपनी सुरक्षा की कामना करते हैं । वे दोनों हम पर इस प्रकार अनुकप्पा करें, जिससे कि हम सुखी रहें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.378)
- **Original**: 169. गन्तारा हि स्थो5वसे ह॒व॑ विप्रस्थ मावत: । धर्तारा चर्षणीनाम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.379)
- **Original**: है इन्द्र और वरुणदेवो ! आप दोनों, मनुष्यों के सप्राट्‌ , धारक एवं पोषक हैं। हम जैसे ब्राह्मणों के आवाहन पर सुरक्षा के लिए आप निश्चय हीं आने को उद्यत रहते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.380)
- **Original**: 170. अनुकामं तर्पयेथामिन्द्रावरूण राय आ। ता वां नेदिष्ठमीमहे
- **Translation**: 

---

