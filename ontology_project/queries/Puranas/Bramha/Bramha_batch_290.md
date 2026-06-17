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

### Verse 1 (Bramha 0.5781)
- **Original**: उनका ही रूप है, ये सदा ही जगत्‌का कल्याण गर्वीले दैत्योंकी अनेक अक्षौहिणी सेनाएँ हैं।
- **Translation**: 

---

### Verse 2 (Bramha 0.5782)
- **Original**: करनेके लिये अपने अंशसे अवतार ले धर्मकी सुरेश्वरो! मैं आपलोगोंकों बताये देती हूँ कि उन स्थापना करते हैं।' दैत्योंके भारी भारसे पीड़ित होनेके कारण अब
- **Translation**: 

---

### Verse 3 (Bramha 0.5783)
- **Original**: यों कहकर ब्रह्माजी सम्पूर्ण देवताओंके साथ मुझमें अपनेको धारण करनेकी भी शक्ति नहीं रह
- **Translation**: 

---

### Verse 4 (Bramha 0.5784)
- **Original**: क्षीरसागरके तटपर गये और एकाग्रचित्त होकर गयी है। अत: आपलोग मेरा भार उतारिये।' । भगवान्‌ गरूड्ध्बजकी स्तुति करने लगे।
- **Translation**: 

---

### Verse 5 (Bramha 0.5785)
- **Original**: » भगवान्‌के अवतारका उपक्रम * 277 ब्रह्मजी बोले--सहस्रमूर्तें! आपको बारंबार
- **Translation**: 

---

### Verse 6 (Bramha 0.5786)
- **Original**: देवकौदेवी हैं, उनके आठवें गर्भसे मेरा यह श्याम नमस्कार है। आपके सहस्रों बाँहें, अनेक मुख
- **Translation**: 

---

### Verse 7 (Bramha 0.5787)
- **Original**: केश प्रकट होगा। भूतलपर अवतीर्ण हो यह और अनेक चरण हैं। आप जगत्‌की सृष्टि, पालन
- **Translation**: 

---

### Verse 8 (Bramha 0.5788)
- **Original**: कालनेमिके अंशसे उत्पन्न हुए कंसका बंध और संहारमें संलग्र रहते हैं। अप्रमेय परमेश्वर!
- **Translation**: 

---

### Verse 9 (Bramha 0.5789)
- **Original**: करेगा।' यों कहकर भगवान्‌ श्रीहरि अन्तर्धान हो आपको बारंबार नमस्कार है। भगवन्‌! आप
- **Translation**: 

---

### Verse 10 (Bramha 0.5790)
- **Original**: गये। अदृश्य हो जानेपर उन परमात्माको प्रणाम सूक्ष्ससे भी अत्यन्त सूक्ष्म, परम महान्‌ और बड़े-
- **Translation**: 

---

### Verse 11 (Bramha 0.5791)
- **Original**: करके सम्पूर्ण देवता मेरुपर्यतके शिखरपर चले बड़े गुरुओंसे भी अधिक गौरवशाली हैं। आप
- **Translation**: 

---

### Verse 12 (Bramha 0.5792)
- **Original**: गये और वहाँसे पृथ्वीपर अवतोर्ण हुए। प्रकृति, समष्टि बुद्धि (महत्तत््व), अहंकार तथा
- **Translation**: 

---

### Verse 13 (Bramha 0.5793)
- **Original**: एक दिन महर्षि नारदने कंससे जाकर वाणीके भी प्रधान मूल हैं। अपरा-प्रकृतिमय
- **Translation**: 

---

### Verse 14 (Bramha 0.5794)
- **Original**: कहा--'देवकीके आठवें गर्भसे भगवान्‌ विष्णु सम्पूर्ण जगत्‌ आपका ही स्वरूप है। आप हमपर
- **Translation**: 

---

### Verse 15 (Bramha 0.5795)
- **Original**: उत्पन्न होंगे, जो तुम्हारा वध करेंगे।' यह सुनकर प्रसन्न होइये। देव! यह पृथ्वी आपको शरणमें
- **Translation**: 

---

### Verse 16 (Bramha 0.5796)
- **Original**: कंसको बड़ा क्रोध हुआ और उसने देवकी तथा आयी है। इस समय भूतलपर जो बड़े-बड़े असुर
- **Translation**: 

---

### Verse 17 (Bramha 0.5797)
- **Original**: वसुदेवको कारागृहमें बंदी बना लिया। वसुदेवने उत्पन्न हुए हैं, उनके द्वारा पीड़ित होनेसे इसके
- **Translation**: 

---

### Verse 18 (Bramha 0.5798)
- **Original**: यह प्रतिज्ञा की थो कि “देवकीके गर्भसे जो-जो पर्वतरूपी बन्धन शिधिल पड़ गये हैं। आप
- **Translation**: 

---

### Verse 19 (Bramha 0.5799)
- **Original**: पुत्र उत्पन्न होगा, उसे मैं स्वयं लाकर दे दिया सम्पूर्ण जगत॒के परम आश्रय हैं। आपकी महिमा
- **Translation**: 

---

### Verse 20 (Bramha 0.5800)
- **Original**: करूँगा।' इसके अनुसार उन्होंने अपना प्रत्येक अपरम्पार है। अतः यह वसुधा अपना भार
- **Translation**: 

---

