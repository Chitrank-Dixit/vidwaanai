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

### Verse 1 (Vaivtpuran 15.8750)
- **Original**: ._ ब्रह्माजी बोले--मैं शान्त, सर्वेश्वर तथा है। वह उत्तम लोक मानो वायुके आधारपर स्थित
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.8751)
- **Original**: अच्युत उन कमलाकान्तको प्रणाम करता हूँ, है। (वास्तवमें वह चिन्मय लोक श्रीहरिसे भिन्न जिनकी हम तौनों विभिन्न कलाएँ हैं तथा समस्त न होनेके कारण अपने-आपमें ही स्थित है।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.8752)
- **Original**: देवता जिनकी कलाकी भी अंशकलासे उत्पन्न उसका दूसरा कोई आधार नहीं है।) उस सनातन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.8753)
- **Original**: हुए हैं। निर्ञन! मनु, मुनीन्द्र, मानव तथा चराचर धामकी स्थिति ब्रह्मलोकसे एक करोड़ योजन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.8754)
- **Original**: प्राणा आपसे ही आपके कलाकी अंशकलाद्वारा ऊपर है। दिव्य रत्लों्वारा निर्मित विचित्र बैकुण्ठधामका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.8755)
- **Original**: प्रकट हुए हैं। वर्णन कर पाना कवियोंके लिये असम्भव है। भगवान्‌ शंकरने कहा--आप अविनाशी पद्मराग और नीलमणिके बने हुए राजमार्ग उस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.8756)
- **Original**: तथा अविकारी हैं। योगीजन आपमें रमण करते धामकी शोभा बढ़ाते हैं। मनके समान तीर गतिसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8757)
- **Original**: हैं। आप अव्यक्त ईश्वर हैं। आपका आदि नहीं है; जानेवाले वे ब्रह्मा, शिव और धर्म सब-के-सब
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8758)
- **Original**: परंतु आप सबके आदि हैं। आपका स्वरूप उस मनोहर वैकुण्ठधाममें जा पहुँचे। श्रीहरिके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8759)
- **Original**: आनन्दमय है। आप सर्वरूप हैं। अणिमा आदि अन्तःपुरमें पहुँचकर उन सबने वहाँ उनके दर्शन
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8760)
- **Original**: सिद्धियोंक कारण तथा सबके कारण हैं। सिद्धिके किये। वे श्रीहरि दिव्य रत्रमय अलक्जारोंसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8761)
- **Original**: ज्ञाता, सिद्धिताता और सिद्धिरूप हैं। आपकी विभूषित हो रलत्नसिंहासनपर बैठे थे। रल्रोंके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8762)
- **Original**: स्तुति करनेमें कौन समर्थ है? बाजूबंद, कंगन और नूपुर उनके हाथ-पैरोंकी धर्म योले--जिस वस्तुका वेदमें निरूपण शोभा बढ़ाते थे। दिव्य रत्नोंके बने हुए दो कुण्डल
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8763)
- **Original**: किया गया है, उसीका विद्वान्‌ लोग वर्णन कर उनके दोनों गालॉपर झलमला रहे थे। उन्होंने [सकते हैं। जिनको बेदमें ही अनिर्वचनीय कहा पीताम्बर पहन रखा था तथा आजानुलम्बिनी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8764)
- **Original**: गया है, उनके स्वरूपका निरूपण कौन कर सकता वनमाला उनके अग्रभागकों विभूषित कर रही
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8765)
- **Original**: है? जिसके लिये जिस वस्तुकी सम्भावना कौ थी। सरस्वतीके प्राणवल्लभ श्रीहरि शान्तभावसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8766)
- **Original**: जाती है, वह गुणरूप होती है। वही उसका स्तवन बैठे थे। लक्ष्मीजी उनके चरणारविन्दोंकी है। जो निरज्ञन (निर्मल) तथा गुणोंसे पृथक्‌--निर्गुण कर रहो थीं। करोड़ों कन्दर्पोंकी लावण्यलीलासे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8767)
- **Original**: हैं; उन परमात्माकी मैं कया स्तुति करूँ?
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.19237)
- **Original**: < 26 » संक्षिम ब्रह्मवैवर्तपुराण * 7:22: 72022: 7 2-:.ल्‍.27::“2222,:334404“-*04,44404444ल्‍++444440.24 वेदों वा पण्डितो वान्य: को वा त्वां स्तोतुमीश्वरः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.19238)
- **Original**: स्तवानां जनके ज्ञानं बुद्द्धिजञनाम्बिका सदा
- **Translation**: 

---

