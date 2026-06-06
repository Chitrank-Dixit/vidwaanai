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

### Verse 1 (Vaivtpuran 8.565)
- **Original**: व्यवस्था की कि एक पक्षमें चन्द्रमा क्रमश:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.566)
- **Original**: रात उनके साथ विहार करने लगे और उसी क्षीण होंगे और दूसरे पक्षमें क्रमशः पुष्ट होते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.567)
- **Original**: दिनसे उनको समभावसे देखने लगे। मुने! इस हुए परिपूर्ण हो जायँंगे। ब्रह्मन्‌! उन सबको वर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.568)
- **Original**: प्रकार मैंने यहाँ सम्पूर्ण सृष्टि-क्रमका कुछ वर्णन देकर श्रीहरि अपने धामकों चले गये और दक्षने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.569)
- **Original**: किया है। इस प्रसड्रको पुष्कर-तीर्थमें चन्द्रमको लेकर उन्हें अपनी कन्याओंको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.570)
- **Original**: मुनियोंकी मण्डलीके बीच गुरुजीके मुखसे मैंने सौंप दिया। चन्द्रमा उन सबको पाकर दिन-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.571)
- **Original**: सुना था। (अध्याय 9) #0885+-- गव्पपथई2 2-2 जाति और सम्बन्धका निर्णय तदनन्तर सौतिने मुनिश्रेष्ठ बालखिल्यादि, यह मैंने भूतलपर जो जातियाँ हैं, उनके बृहस्पति, उतथ्य, पराशर, विश्रवा, कुबेर, रावण,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.572)
- **Original**: निर्णयके विषयमें कुछ बातें बतायी हैं। बर्णसंकर- कुम्भकर्ण, महात्मा विभीषण, बात्स्य, शाण्डिल्य,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.573)
- **Original**: दोषसे और भी बहुत-सी जातियाँ हो गयी हैं। सावर्णि, कश्यप तथा भरद्वाज आदिकी; ब्राह्मण,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.574)
- **Original**: सभी जातियोंमें जिनका जिनके साथ सर्वथा क्षत्रिय, वैश्य, शूद्र और अनेकानेक वर्णसंकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.575)
- **Original**: सम्बन्ध है, उनके विषयमें मैं वेदोक्त तत्त्वका जातियोंकी उत्पत्तिक प्रसंग सुनाकर कहा-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.576)
- **Original**: बर्णन करता हँ--जैसा कि पूर्वकालमें ब्रह्माजीने अश्विनीकुमारके द्वारा एक ब्राह्मणीके गर्भसे पुत्रकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.577)
- **Original**: कहा था। पिता, तात और जनक--ये शब्द उत्पत्ति हुई। इससे उस ब्राह्मणीके पतिने पुत्रसहित
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.578)
- **Original**: जन्मदाताके अर्थमें प्रयुक्त होते हैं। अम्बा, माता, पत्नीका त्याग कर दिया। ब्राह्मणी दुःखित हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.579)
- **Original**: जननी और प्रसू-इनका प्रयोग गर्भधारिणीके योगके द्वारा देह त्यागकर गोदाबरी नामकी नदी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.580)
- **Original**: अर्थमें होता है। पिताके पिताकों पितामह कहते हो गयी। सूर्यनन्दन अश्विनीकुमारने स्वयं उस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.581)
- **Original**: हैं और पितामहके पिताकों प्रपितामह। इनसे पुत्रकों यत्रपूर्वक चिकित्सा-शास्त्र, नाना प्रंकारके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.582)
- **Original**: ऊपरके जो कुटुम्बीजन हैं, उन्हें सगोत्र कहा गया शिल्प तथा मन्त्र पढ़ाये। किंतु वह ब्राह्मण निरन्तर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.583)
- **Original**: है। माताके पिताको मातामह कहते हैं, मातामहके नक्षत्रोंकी गणना करने और बेतन लेनेसे बैदिक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.584)
- **Original**: पिताकी संज्ञा प्रमातामह है और प्रमातामहके धर्मसे भ्रष्ट हो इस भूतलपर गणक हो गया।
- **Translation**: 

---

