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

### Verse 1 (Vaivtpuran 22.18820)
- **Original**: आणिमादिकसिद्धीश सिद्धे: सिद्धधिस्वरूपक । तपस्तपस्विस्तपसां बीजरूप नपमरोउस्तु ते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.18821)
- **Original**: यदनिर्वचचनीयं च वस्तु निर्वचनीयकम्‌ । तत्स्वरूप तयोबीज सर्वबीज नमो5स्तु ते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.18822)
- **Original**: अहं सरस्वती लक्ष्मीदुर्गा गड्ढा श्रुतिप्रसू:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.18823)
- **Original**: यस्य पादार्चनान्नित्यं पूज्या तस्मै नमो नमः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.18824)
- **Original**: स्पर्शने यस्य भृत्यानां ध्याने चापि दिवानिशम्‌ । प्रवित्राणि च तीर्थानि तस्मैँ भगवते नम:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1407)
- **Original**: ब्रह्माजीसे सृष्टिके लिये दारपरिग्रहकी प्रेरणा पाकर डरे हुए नारदका स्त्री-संग्रहके दोष बताकर तपके लिये जानेकी आज्ञा माँगना सौति कहते हैं--सृश्टिकर्ता ब्रह्माने अपने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1408)
- **Original**: भोग्या और कुलटा। वे सब-कौ-सब स्वार्थपरायणा सब बालकोंको सृष्टिके कार्यमें लगाकर नारदजीको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1409)
- **Original**: होती हैं। साध्वी स्त्री परलोकके भवसे, इस भी सृष्टि करनेके लिये प्रेरित किया। उन्होंने लोकमें अपनेकों यश मिलनेके लोभसे तथा बेद-वेदाड्लोंके पारंगत बिद्वान्‌ नारदसे यह सत्य,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1410)
- **Original**: कामासक्तिसे भी निरन्तर स्वामीकी सेवा करती हितकर, वेदसारस्वरूप और परिणाममें सुख
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1411)
- **Original**: है। भोग्या स्त्री भोगकी अभिलाषिणी होती है। देनेबाली बात कही। बह सदा केवल कामासक्तिसे ही प्रियतम पतिकी ख्रह्मजी बोले--कुलमें श्रेष्ठ मेरे प्राणवल्लभ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1412)
- **Original**: सेवा करती है। भोगके सिवा और किसी हेतुसे पुत्र नाद! आओ। तुम ज्ञानदीपकी शिखासे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1413)
- **Original**: वह क्षणभर भी सेवा नहीं करती। भोग्या स्त्री अज्ञानान्धकारका निवारण करनेवाले हो+ तुमसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1414)
- **Original**: जबतक वस्त्र, आभूषण, सम्भोग तथा सुस्निग्ध यह बात छिपी नहीं है कि जन्मदाता पिता परम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1415)
- **Original**: एवं उत्तम आहार पाती है, तबतक ही स्वामीके गुरु है। वह सभी वन्दनीय पुरुषोंमें सबसे श्रेष्ठ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1416)
- **Original**: वशमें रहकर प्यारी बनी रहती है। कुलटा नारी है। विद्यादाता और मन्त्रदाता दोनों समान हैं तथा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1417)
- **Original**: कुलमें अंगारके समान है। वह कुलका नाश पितासे भी बढ़कर हैं। बेटा! मैं तुम्हारा पिता,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1418)
- **Original**: करनेवाली है। कुलटा स्त्री कपटसे ही स्वामीकी पालक, विद्यादाता एवं मन्त्रदाता भी हूँ। तुम मेरी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1419)
- **Original**: सेवा करती हैं, भक्तिसे नहीं। वे अपने स्वार्थकी आज्ञासे मेरी ही प्रसन्नताके लिये विवाह कर लो।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1420)
- **Original**: सिद्धिके लिये सुधाके समान मधुर वचन बोलती ब्रह्माजीकी यह बात सुनकर मुनिवर नारदके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1421)
- **Original**: हैं। क्रोध होनेपर उनके मुखसे विषके समान कण्ठ, ओठ और तालु सूख गये। वे भयभीत
- **Translation**: 

---

