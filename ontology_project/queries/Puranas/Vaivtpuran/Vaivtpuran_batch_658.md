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

### Verse 1 (Vaivtpuran 67.5955)
- **Original**: वे चार भुजाधारी भगवान्‌ विष्णु लक्ष्मी तथा तज्लीन थे कि उन्हें रात-दिनका आना-जाना ज्ञात
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.5956)
- **Original**: पार्षदोंके साथ बहुत-सी सामग्री लिये हुए रत्नजटित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.5957)
- **Original**: +* गणपतिखण्ड «» 301 अंकककक़कक़
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.5958)
- **Original**: ऋऊ कक $
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.5959)
- **Original**: 4 ## 6 # ## ### ##ऋ#ऋ#ऋ$%$%$%$%%%% 4 ###6##&##%%#$ 5555 ####6####$5%$5% विमानपर आरूढ़ हो वहाँ उपस्थित हुए तत्पश्चात्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.5960)
- **Original**: सुसज्जित था। उपस्थित सारा जन-समुदाय सनक, सनन्‍्दन, सनातन, कपिल, आसुरि, क्रतु,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.5961)
- **Original**: आनन्दपूर्वकः उसे निहार रहा था। सारे हँस, वोढु, पश्रशिख, आरुणि, यति, सुमति,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.5962)
- **Original**: कैलासवासी परमानन्दमें निमग्र थे। अनुयायियोंसहित वसिष्ठ, पुलह, पुलस्त्य, अत्रि, तदनन्तर शंकरजीने समागत अतिथियोंको भृगु, अद्विरा, अगस्त्य, प्रचेता, दुर्वासा, च्यवन,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.5963)
- **Original**: ऊँचे-ऊँचे सिंहासनोंपर बैठाकर उनका आदर- मरीचि, कश्यप, कण्व, जरत्कारु, गौतम, बृहस्पति,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.5964)
- **Original**: सत्कार किया। पार्वतीके इस ब्रतमें इन्द्र दानाध्यक्ष, उतध्य, संवर्त, सौभारि, जाबालि, जमदग्नि, जैगीषव्य,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.5965)
- **Original**: कुबेर कोषाध्यक्ष, स्वयं सूर्य आदेश देनेवाले और देवल, गोकामुख, वक्ररथ, पारिभद्र, पराशर,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.5966)
- **Original**: वरुण परोसनेके कामपर नियुक्त थे। उस समय विश्वामित्र, वामदेव, ऋष्यभ्रृद्र, विभाण्डक,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.5967)
- **Original**: दही, दूध, घृत, गुण, चीनी, तेल और मधु मार्कण्डेय, मृकण्डु, पुष्कर, लोमश, कौत्स, वत्स,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.5968)
- **Original**: आदिकी लाखों नदियाँ बहने लगी थीं। इसी दक्ष, बालाग्रि, अघमर्षण, कात्यायन, कणाद,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.5969)
- **Original**: प्रकार गेहूँ, चावल, जौ और चिठरे आदिके पाणिनि, शाकटायन, शक्कर, आपिशलि, शाकल्य,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.5970)
- **Original**: पहाड़ों-के-पहाड़ लग गये थे। महामुने ! पार्वतीके शद्भु--ये तथा और भी बहुत-से मुनि शिष्योंसहित
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.5971)
- **Original**: ब्रतमें कैलास पर्वतपर सोना, चाँदी, मूँगा और वहाँ पधारे। मुने ! धर्मपुत्र नर-नारायण भी आये।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.5972)
- **Original**: मणियोंके पर्वत-सरीखे ढेर लगे हुए थे। लक्ष्मीने पार्वतीके उस ब्रतमें दिकूपाल, देवता, यक्ष,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.5973)
- **Original**: भोजन तैयार किया था, जिसमें परम मनोहर खीर, गन्धर्व, किन्नर और गणोंसहित सभी पर्वत भी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.5974)
- **Original**: पूड़ी, अगहनीका चाबल और घृतसे बने हुए उपस्थित हुए। शैलराज हिमालय, जो अनन्त
- **Translation**: 

---

