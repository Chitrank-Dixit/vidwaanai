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

### Verse 1 (Mahabharat 0.5481)
- **Original**: दिया। तत्पश्षात्‌ उन्होंने नकुछ, सहदेव, भीमसेन और ही थे नकुल और सहदेवसे भी भिड़े हुए थे । जब झल्य अपने
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5481)
- **Original**: दिया। तत्पश्षात्‌ उन्होंने नकुछ, सहदेव, भीमसेन और ही थे नकुल और सहदेवसे भी भिड़े हुए थे । जब झल्य अपने
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5482)
- **Original**: युथिष्ठिस्‍्को भी दस बाणोंसे घायछ किया। इस महान बाणोंसे पाण्डव-महारधियोंको आहत कर रहे थे, उस समय
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5482)
- **Original**: युथिष्ठिस्‍्को भी दस बाणोंसे घायछ किया। इस महान बाणोंसे पाण्डव-महारधियोंको आहत कर रहे थे, उस समय
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5483)
- **Original**: संप्राममें यैंने शल्यका अद्भुत पराक्रम देखा; ये अकेले उन्हें कोई अपना रक्षक नहीं दिखायी देता था।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5483)
- **Original**: संप्राममें यैंने शल्यका अद्भुत पराक्रम देखा; ये अकेले उन्हें कोई अपना रक्षक नहीं दिखायी देता था।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5484)
- **Original**: ही पाण्डबॉके समस्त योद्धाओंके साथ युद्ध कर इसी समय झूरवीर नकुलने अपने मामा (शल्य) पर रहे थे। बड़े बेगसे धावा किया और बाणोंकी वर्षासे उन्हें आच्छादित तदनत्तर वे युथिष्ठिरके बहुत निकट आ गये और उन्हें कर दिया। फिर हैसते-हैसते उसने दस बाणोंसे शल्यकी छाती
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5484)
- **Original**: ही पाण्डबॉके समस्त योद्धाओंके साथ युद्ध कर इसी समय झूरवीर नकुलने अपने मामा (शल्य) पर रहे थे। बड़े बेगसे धावा किया और बाणोंकी वर्षासे उन्हें आच्छादित तदनत्तर वे युथिष्ठिरके बहुत निकट आ गये और उन्हें कर दिया। फिर हैसते-हैसते उसने दस बाणोंसे शल्यकी छाती
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5485)
- **Original**: अपने बाणोंसे पीड़ित करके पुनः भीमपर दूट पड़े। उस
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5485)
- **Original**: अपने बाणोंसे पीड़ित करके पुनः भीमपर दूट पड़े। उस
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5486)
- **Original**: समय राजा झल्यकी फुर्ती तथा अख-संचालनकी कुझलता देखकर आपके तथा झजुपक्षके योद्धाओंने उनकौ बहुत
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5486)
- **Original**: समय राजा झल्यकी फुर्ती तथा अख-संचालनकी कुझलता देखकर आपके तथा झजुपक्षके योद्धाओंने उनकौ बहुत
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5487)
- **Original**: प्रशंसा कौ। शल्यके बाणोंसे अत्यन्त घायल होकर जब पाण्डब-योद्धा बहुत कष्ट पाने लगे तो युधिष्ठिस्के पुकारने और मना करनेपर भी वे युद्धका मैदान छोड़कर भाग
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5487)
- **Original**: प्रशंसा कौ। शल्यके बाणोंसे अत्यन्त घायल होकर जब पाण्डब-योद्धा बहुत कष्ट पाने लगे तो युधिष्ठिस्के पुकारने और मना करनेपर भी वे युद्धका मैदान छोड़कर भाग
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5488)
- **Original**: चले। इससे धर्मराजको बड़ा अमर्ष हुआ, उत्होंने निक्षय कर लिया कि “मेरी विजय हो या मृत्यु, युद्ध अवश्य
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5488)
- **Original**: चले। इससे धर्मराजको बड़ा अमर्ष हुआ, उत्होंने निक्षय कर लिया कि “मेरी विजय हो या मृत्यु, युद्ध अवश्य
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5489)
- **Original**: कहूँगा।' फिर तो बे अपने पुरुषार्थका भरोसा करके कह और अपने सब भाइयोंको बुलाकर बोले--'मैं अपने
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5489)
- **Original**: कहूँगा।' फिर तो बे अपने पुरुषार्थका भरोसा करके कह और अपने सब भाइयोंको बुलाकर बोले--'मैं अपने
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5490)
- **Original**: मनकी बात बताता हूँ। मेरे पहियोंकी रक्षा करनेवाले
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5490)
- **Original**: मनकी बात बताता हूँ। मेरे पहियोंकी रक्षा करनेवाले
- **Translation**: 

---

