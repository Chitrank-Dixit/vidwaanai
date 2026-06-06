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

### Verse 1 (Vaivtpuran 7.9793)
- **Original**: श्रीहरिको देखकर पत्नीसहित नन्दको बड़ी प्रसन्नता विभूषित गोपियाँ जय-जयकार करने लगीं। उस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9794)
- **Original**: हुई। धायने ठंढे जलसे बालकको नहलाया और पराये पुत्रके लिये भी नन्‍्दने बड़े आदरके साथ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9795)
- **Original**: उसकी नाल काट दी। उस समय गोपियाँ हर्षसे महान्‌ उत्सव मनाया। यशोदाजीने गोपियों तथा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9796)
- **Original**: जय-जयकार करने लगीं। त्रजकी सारी गोपिकाएँ, ब्राह्मणियोंको प्रसन्नतापूर्वक धन दान किया। नाना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9797)
- **Original**: बालिका और युठतियाँ भी ब्राह्मणपत्नियोंके साथ प्रकारके द्रव्य, सिन्दूर एवं तैल प्रदान किये।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9798)
- **Original**: सूतिकागारमें आयां। उन सबने आकर बालककों
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9799)
- **Original**: * श्रीकृष्णजन्मखण्ड * है. 3.34 544 4
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9800)
- **Original**: 40000040.044 04000. 0400044 40000 400 00000 0040 0400 44 4 4 4 44444 4 44.44. देखा और प्रसन्नतापूर्वक उसे आशीर्वाद दिया।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9801)
- **Original**: दान करके नन्दजी बड़े प्रसन्न हुए। उन्होंने नन्दनन्दनकी भूरि-भूरि प्रशंसा करती हुई वे उन्हें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9802)
- **Original**: [सूतिकागारकी रक्षाके लिये ब्राह्मणोंको नियुक्त अपनी गोदमें ले लेती थीं। उनमेंसे कितनी ही
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9803)
- **Original**: किया। मन्त्रज्ञ मनुष्यों तथा बड़ी-बूढ़ी गोपियोंको 224 लगाया। उन्होंने ब्राह्मणोंद्वारा वेदोंका पाठ कराया। एकमात्र मड्गलमय हरिनामका कीर्तन कराया तथा देवताओंकी पूजा करवायी। युवती तथा बड़ी-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9804)
- **Original**: बूढ़ी ब्राह्मणपत्रियाँ बालक-बालिकाओंको साथ 4 ले मुस्कराती हुई नन्दभवनमें आयीं। नन्दरायजीने उनको भी नाना प्रकारके धन और रत्न दिये। (
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9805)
- **Original**: रत्रमय अलंकारोंसे विभूषित बड़ी-बूढ़ी गोपियाँ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9806)
- **Original**: भी मुस्कराती हुई तीज्र गतिसे नन्द-मन्दिरमें आयों। उन्हें बहुत-से वस्त्र, चाँदी और सहस्रो गौएँ सादर अर्पित कीं। ज्यौतिष-शास्त्रके विशेषज्ञ 9 6 विविध ज्यौतिषी, जिनकी वाणी सिद्ध थी, हाथमें किक पुस्तकें लिये नन्दमन्दिरमें पधारे। नन्दजीने उन्हें नमस्कार करके प्रसन्नतापूर्वक उनके सामने विनय प्रकट की। उन सबने आशीर्वाद दिये और उत्तम नन्‍्दने वस्त्रसहित स्नान करके धुली हुई बालकको देखा। इस प्रकार ब्रजराज नन्दने धोती और चादर धारण की। फिर प्रसन्नचित्त हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9807)
- **Original**: सामग्री एकत्र करके पुन्रोत्सत मनाया और वहाँ परम्परागत विधिका पालन किया। ब्राह्मणोंको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9808)
- **Original**: ज्यौतिषियोंद्रार शुभाशुभ भविष्यका प्रकाशन कराया। भोजन कराया, उनसे मज्जलपाठ करवाया, नाना
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9809)
- **Original**: तदनन्तर वह बालक नन्दभवनमें शुक्ल पक्षके प्रकारके बाजे बजवाये और वन्दीजनोंकों धन-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9810)
- **Original**: चन्द्रमाकी भाँति दिनोंदिन बढ़ने लगा। श्रीकृष्ण दान किया। तत्पश्चात्‌ नन्दने आनन्दपूर्वक ब्राह्मणोंको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9811)
- **Original**: और हलधर दोनों ही माताका स्तन-पान करते धन दिया तथा उत्तम रत्न, मूँगे और हीरे भी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9812)
- **Original**: थे। मुने! वहाँ नन्‍्दके पुत्रोत्सवर्में प्रसन्न हुई आदरपूर्वक उन्हें दिये। मुने! तिलोंके सात पर्वत,
- **Translation**: 

---

