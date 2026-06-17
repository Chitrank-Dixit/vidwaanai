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

### Verse 1 (Vaivtpuran 543.17554)
- **Original**: क्या सुनना चाहते हो ? (अध्याय 128) 4-08 स्य 0 409,00007
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17555)
- **Original**: नारायणके आदेशसे नारदका विवाहके लिये उद्यत हो ब्रह्मलोकमें जाना, ब्रह्माका दल-बलके साथ राजा सुंजयके पास आना, सुंजय-कन्या और नारदका विवाह, सनत्कुमारद्वारा नारदको श्रीकृष्ण-मन्त्रोपदेश, महादेवजीका उन्हें श्रीकृष्णका ध्यान और जप-विधि बतलाना, तपके अन्तमें नारदका शरीर त्यागकर श्रीहरिके पादपद्यमें लीन होना नारदने कहा--महाभाग! मेरी जो कुछ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17556)
- **Original**: नारायणको प्रणाम करके शीघ्र ही राजा सृंजयकी सुननेकी लालसा थी; वह सब कुछ सुन लिया। राजधानीकी ओर चल दिये। अब कुछ भी अवशिष्ट नहीं है। कामनाकी शौनकने कहा--महाभाग सूतजी! अहो, पूर्ति करनेबाला यह ब्रह्मबैवर्तपुराण कैसा अद्भुत यह कैसा परम अद्भुत, पुरातन, सरस, अपूर्व है! जगदगुरो! मैं तप करनेके लिये हिमालयपर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17557)
- **Original**: रहस्य है! इसे तो मैंने सुन लिया। अब मैं जाना चाहता हूँ, इसके लिये मुझे आज्ञा दीजिये।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17558)
- **Original**: नारदका विवाह-वृत्तान्त सुनना चाहता हूँ; क्योंकि अथवा अब मैं क्‍या करूँ, वह मुझे बतलानेकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17559)
- **Original**: नारदमुनि तो अतीन्द्रिय और ब्रह्माके पुत्र थे। कृपा करें।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17560)
- **Original**: . सूतजी कहते हैं--शौनक! नारदपर मोहने श्रीनारायण बोले--तारद! इस समय तो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17561)
- **Original**: अपना अधिकार जमा लिया था; अत: बे विष्णु- तुम ब्रह्माके पुत्र हो; परंतु पूर्वजन्ममें तुम उपबर्हण
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17562)
- **Original**: ब्रतपरायणा महाभागा तपस्विनी सूंजय-कन्याको नामक गन्धर्व थे। तुम्हारे पचास पत्िियाँ थीं।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17563)
- **Original**: देखकर ब्रह्माजीकी रमणीय सभामें गये। वह सभा उनमेंसे एक सती-साध्बी सुन्दरी कामिनीने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17564)
- **Original**: सभी देवताओंसे खचाखच भरी थी। वहाँ उन्होंने तपस्थाद्वारा भगवान्‌ शंकरकी आराधना की और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17565)
- **Original**: पिता ब्रह्माको प्रणाम करके उनसे सारा रहस्य बररूपमें नारदकों अपना मनोनीत पति प्राप्त
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17566)
- **Original**: कह सुनाया। उस शुभ समाचारकों सुनकर किया। वही राजा सूंजयकी कन्या होकर पैदा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17567)
- **Original**: ब्रह्माका मुख प्रसन्नतासे खिल उठा। फिर तो हुई है। उसका नाम स्वर्णबी (स्वर्णष्टीवी) है।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17568)
- **Original**: जगत्पति ब्रह्मा अपने तपस्वी पुत्र नारदसे बातचीत वह इच्छाकी सहोदरा बहिन है। वह सुन्दरियोंमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17569)
- **Original**: करके शुभ मुहूर्तमें देवताओंके साथ पुत्रकों आगे परम सुन्दरी, कोमलाड़ी, लक्ष्मीकी कला, पतिब्रता,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17570)
- **Original**: करके रत्ननिर्मित विमानद्वारा सृंजवके महलकों महाभागा, मनोहरा, अत्यन्त प्रिय बोलनेवाली,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17571)
- **Original**: चल पड़े। उस समाचारको सुनकर राजा सूंजयने कामुकी, कमनीया और सदा सुस्थिर यौजनवाली
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17572)
- **Original**: अपनी रत्ननिर्मित आभूषणोंसे विभूषित सुन्दरी है। तुम उसके साथ विवाह कर लो; क्योंकि
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17573)
- **Original**: कन्‍्याकों लेकर हर्षपूर्वक नारदकों सौंप दिया। शंकरकी आज्ञा व्यर्थ कैसे हो सकती है? ब्रह्माने। साथ हो अपना सारा मणिमुक्ता आदि दहेजमें जो प्राक्तन कर्म लिख दिया है; उसे कौन मिटा
- **Translation**: 

---

