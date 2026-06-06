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

### Verse 1 (Vaivtpuran 75.9208)
- **Original**: पालकका भी पालक परात्पर परमेश्वर हूँ। मेरी समयपर ही वे कच्चे फलोंसे युक्त होते हैं। सुख-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 75.9209)
- **Original**: आज्ञासे ये शिव संहार करते हैं; इसलिये इनका दुःख, सम्पत्ति-विपत्ति, शोक-चिन्ता तथा शुभ-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 75.9210)
- **Original**: नाम “हर' है। तुम मेरे आदेशसे सृष्टिके लिये अशुभ--सब अपने-अपने कर्मोंके फल हैं और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 75.9211)
- **Original**: उद्यत रहते हो; इसलिये 'विश्वद्नष्टा' कहलाते हो सभी समयपर ही उपस्थित होते हैं । तीनों लोकॉमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 75.9212)
- **Original**: और धर्मदेव रक्षाके कारण ही 'पालक' कहलाते न तो कोई किसीका प्रिय है और न अप्रिय
- **Translation**: 

---

### Verse 6 (Vaivtpuran 75.9213)
- **Original**: हैं। ब्रह्मासे लेकर तृणपर्यन्त सबका ईश्वर मैं ही ही है। समय आनेपर कार्यवश सभी लोग अप्रिय
- **Translation**: 

---

### Verse 7 (Vaivtpuran 75.9214)
- **Original**: हूँ। मैं ही कर्मफलका दाता तथा कर्मोंका निर्मूलन अथवा प्रिय होते हैं। तुमलोगोंने देखा है, पृथ्वीपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 75.9215)
- **Original**: करनेवाला हूँ। मैं जिनका संहार करना चाहूँ, बहुत-से राजा और मनु हुए और वे सभी अपने-
- **Translation**: 

---

### Verse 9 (Vaivtpuran 75.9216)
- **Original**: उनकी रक्षा कौन कर सकता है? तथा मैं जिनका अपने कर्मोंके फलके परिपाकसे कालके अधीन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 75.9217)
- **Original**: पालन करूँ, उनको मारनेवाला भी कोई नहीं है। हो गये। तुमलोगोंका यहाँ गोलोकमें जो एक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 75.9218)
- **Original**: मैं सबका सृजन, पालन और संहार करता हूँ। क्षण व्यतीत हुआ है, उतनेमें ही पृथ्वीपर सात
- **Translation**: 

---

### Verse 12 (Vaivtpuran 75.9219)
- **Original**: परंतु मेरे भक्त नित्यदेही हैं। उनके संहारमें मैं मन्वन्तर बीत गये। सात इन्द्र समाप्त हो गये।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 75.9220)
- **Original**: भी समर्थ नहीं हूँ। भक्त सदा मेरे पीछे चलते इस समय आठवें इन्द्र चल रहे हैं। इस प्रकार
- **Translation**: 

---

### Verse 14 (Vaivtpuran 75.9221)
- **Original**: हैं और मेरे चरणोंकी आराधनामें तत्पर रहते हैं; मेरा कालचक्र दिन-रात भ्रमण करता रहता है। अत: मैं भी सदा भक्तोंक निकट उनकी रक्षाके इन्द्र, मनु तथा राजा सभी लोग कालके वशीभूत
- **Translation**: 

---

### Verse 15 (Vaivtpuran 75.9222)
- **Original**: लिये मौजूद रहता हूँ। ब्रह्माण्डमें सभी नष्ट होते हो गये। उनकी कीर्ति, पृथ्वी, पुण्य और पापकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 75.9223)
- **Original**: और बारंबार जन्म लेते हैं; परंतु मेरे भक्तोंका नाश कथामात्र शेष रह गयी है। इस समय भी भूमिपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 75.9224)
- **Original**: नहीं होता है। वे सदा निःशड्ढडू और निरापद रहते बहुत-से राजा दुष्ट और भगवत्निन्दक हैं। उनके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 75.9225)
- **Original**: हैं। इसीलिये समस्त विद्वान्‌ पुरुष मेरे दास्यभावकी बल और पराक्रम महान्‌ हैं। परंतु समयानुसार
- **Translation**: 

---

### Verse 19 (Vaivtpuran 75.9226)
- **Original**: अभिलाषा रखते हैं; दूसरे किसी बरकी नहीं। जो वे सब-के-सब कालान्तक यमके ग्रास हो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 75.9227)
- **Original**: मुझसे दास्यभावकी याचना करते है; वे धन्य हैं। जायँगे। यह काल इस समय भी मेरी आज्ञासे दूसरे सब-के-सब वज्ञित हैं। जन्म, मृत्यु, जरा, उपस्थित है। वायु मेरी आज्ञा मानकर ही निरन्तर
- **Translation**: 

---

