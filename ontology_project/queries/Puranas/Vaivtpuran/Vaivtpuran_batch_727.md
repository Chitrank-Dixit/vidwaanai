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

### Verse 1 (Vaivtpuran 543.12854)
- **Original**: धारण करते हैं? अग्निशुद्ध दिव्य वस्त्रको त्यागकर गोलोकके सम्पूर्ण निवासी मेरे समस्त ऐश्वर्यके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12855)
- **Original**: व्याप्रचर्म क्यों पहनते हैं? पारिजात छोड़कर अधिदेवता हैं। तुम सदा मेरे प्राणोंकी अधिप्ठात्री
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12856)
- **Original**: धतूरके फूल क्यों धारण करते हैं ? उन्हें मस्तकपर देवी एवं प्राणोंसे भी अधिक प्यारी हो।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12857)
- **Original**: रत्रमय किरीट धारण करनेकी इच्छा क्‍यों नहां गोपाडनाएँ तुम्हारी कलाएँ हैं; अतएव मुझे प्यारी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12858)
- **Original**: होती ? जटापर ही उनकी अधिक प्रीति क्‍यों है? हैं। गोलोकनिवासी समस्त गोप मेरे रोमकूपसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12859)
- **Original**: दिव्यलोक छोड़कर उन प्रभुको श्मशानमें उत्पन्न हुए हैं। सूर्य मेरे तेज और वायु मेरे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12860)
- **Original**: रहनेकी अभिलाषा क्यों होती है? चन्दन, अगुरु, प्राण हैं। वरुण जलके अधिदेवता तथा पृथ्वी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12861)
- **Original**: कस्तूरी तथा सुगन्धित पुष्पोंकों छोड़कर वे मेरे मलसे प्रकट हुई है। मेरे शरीरका शून्यभाग
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12862)
- **Original**: बिल्वपत्र तथा बिल्व-काष्ठके अनुलेपनकी स्पृहा ही महाकाश कहा गया है। कामकी उत्पत्ति मेरे [क्यों रखते हैं? मैं यह सब जानना चाहती हूँ। मनसे हुई है। इन्द्र आदि सब देवता मेरी कलाके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12863)
- **Original**: प्रभो! आप विस्तारके साथ इसका वर्णन करें। अंशांशसे प्रकट हुए हैं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12864)
- **Original**: सृष्टिक बीजरूप जो महत्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12865)
- **Original**: नाथ! इसे सुननेके लिये मेंरे मनमें कौतृहल बढ़ आदि तत्त्व हैं, उन सबका बीजरूप आश्रयहीन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12866)
- **Original**: रहा है। इच्छा जाग उठी है। आत्मा मैं स्वयं ही हूँ। कर्ममोगका अधिकारी। राधिकाकी यह बात सुनकर मधुसूदनने जीव मेरा प्रतिबिम्ब है। मैं साक्षी और निरीह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12867)
- **Original**: हँसते हुए उन्हें अपने समीप बिठा लिया और हूँ। किसी कर्मका भोगी नहों हूँ। मुझ स्वेच्छामय
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12868)
- **Original**: कथा कहना आरम्भ किया। परमेश्वरका यह शरीर भक्तोंके ध्यानके लिये है।। श्रीकृष्ण बोले--प्रिये! पूर्णतम महेश्वरने एकमात्र परात्पर परमेश्वर मैं ही प्रकृति हूँ और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12869)
- **Original**: साठ हजार युगोंतक तप करते हुए मनके द्वारा मैं ही पुरुष हूँ। सानन्द मेरा ध्यान किया। तत्पश्चात्‌ वे तपस्यासे श्रीराधिकाने पूछा--भगवन्‌! आप सब
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12870)
- **Original**: विरत हो गये। इसी बीच उन्होंने मुझे अपने तत्त्वोंके ज्ञाता, सबके बीज और सनातन पुरुष
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12871)
- **Original**: सामने खड़ा देखा। अत्यन्त कमनीय अन्ज, हैं। समस्त संदेहोंका निवारण करनेवाले प्रभो! [किशोर अवस्था और परम उत्तम श्यामसुन्दर मेरे अभीष्ट प्रश्नवा समाधान कौजिये। भगवान्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12872)
- **Original**: रूप-सब कुछ अनिर्वचनीय था। मेरे उस रूपको शंकर सम्पूर्ण ज्ञानॉंक अधिदेवता, समस्त तत्त्वोंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12873)
- **Original**: देखकर त्रिलोचनके लोचन तृप्त न हो सके। वे ज्ञाता, मृत्युझ्य, कालके भी काल तथा आपके
- **Translation**: 

---

