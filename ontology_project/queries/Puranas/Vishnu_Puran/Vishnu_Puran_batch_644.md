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

### Verse 1 (Vishnu Puran 0.12861)
- **Original**: वहाँ यम्ादि गुणोंसे युक्त होकर एकाप्रच्त्तसे ध्यान करते हुए राजा खाण्डिक्य विष्णु नामक निर्मल ख्ह्ममें लीन हो +# यद्यपि खाण्डिक्य उस समय राजा नहीं धा; तथापि वबनमें जो उसके दुर्ग, मन्‍ल्नी और भृत्य आदि थे उन्हींका स्वामी अपने पुक्रको बनाया ।
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12862)
- **Original**: ड्ए्टड श्रीविष्णुपुराण [ अ> 8 केशिध्वजो विमुक्‍्त्यर्थ स्वकर्मक्षपणोन्प्ुस्वः । गये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12863)
- **Original**: किन्तु केशिध्यज, विदेहमुक्तिके ल्यि अपने सकल्याणोपभोगैश्व क्षीणपापो5मलस्तथा । इच्छा न करके अनेकों गश़ुभ-कर्म किये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12864)
- **Original**: हे द्विज ! इस प्रकार अनेकों कल्याणप्रद भोगोंको भोगते हुए उन्होंने पाप और मल (प्रारब्य-कर्म) का क्षय हो जानेपर ताफयकों दूर अवाप सिद्धिमत्यन्तां तापक्षयफलां द्विज
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12865)
- **Original**: करनेवाली आत्यन्तिक सिद्धि प्राप्त कर ली
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12866)
- **Original**: कनन-+ है 3 बा. इति श्रीविष्णुपुराणे षह्टेंडशे सप्तमोउघ्याय:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12867)
- **Original**: _अफन्‍न्‍न्‍म. है. 5 सामान आठवाँ अध्याय झिष्यपरम्परा, माहात्य्य और उपसंहार श्रीपराज्र उवाच इत्येष कथित: सम्यक्‌ तृतीय: प्रतिसझ़्र: । आल्यन्तिको विमुक्तियाँ लयो ब्रह्मणि झाश्रते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12868)
- **Original**: 1 सर्गश्न प्रतिसर्गश्न॒ वंश्यमन्वन्तराणि च। बंशानुचरित॑ चैव भवतो गदितं मया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12869)
- **Original**: 2 पुराणं वैष्णवं चैतत्सर्वकिल्बिषनाशनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12870)
- **Original**: विशिष्ट सर्वशास््रेभ्य: पुरुषार्थोपपादकम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12871)
- **Original**: 3 तुभ्य॑ यथावन्पैत्रेय प्रोक्ते शुश्रूषवेउव्यथम्‌ । यदन्यदपि वक्तव्य तत्यृच्छाद्य बदामि ते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12872)
- **Original**: 4 अ्रीमैत्रेय उवाच भगवन्कथितं सर्व यत्यृष्टोडसि मया मुने । ध्रुतत चेतन्पया भकत्या नान्यत्प्रष्टव्यमस्ति मे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12873)
- **Original**: 5 विच्छिन्नाः सर्वसन्देहा वैमल्यं मनस: कृतम्‌ । त्वत्प्रसादान्पया ज्ञाता उत्पत्तिस्थितिसंक्षया:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12874)
- **Original**: 6 ज्ातश्षतुर्विधो राशि: झक्तिश्न त्रिविधा गुरो। विज्ञाता सा च कार्त्स्येन त्रिविधा भावभावना
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12875)
- **Original**: 7 त्वव्मसादान्यया ज्ञातं ज्ञेयप्रन्यैरल द्विज । भ्रीपराज्षरजी बोल्छे--हे मैत्रेय ! इस प्रकार मैंने तुमसे तीसरे आत्यन्तिक प्रकूयका वर्णन किया, जो सनातन ब्रहामें लवरूप मोक्ष ही है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12876)
- **Original**: मैंने तुमसे संसारकी उत्पत्ति, प्रकय, वंश, मन्वन्तर तथा वंदॉकि चरित्रोंका वर्णन किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12877)
- **Original**: हे मैत्रेय ! मैंने तुम्हें सुननेके लिये उत्सुक देखकर यह सम्पूर्ण द्ास्त्रोमें ओेप्ट सर्वपापविनाशक और पुरुषार्थका प्रतिपादक वैष्णवपुराण सुना दिया । अब तुम्हें जो और कुछ पूछना हो पूछो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12878)
- **Original**: मैं उसका तुमसे वर्णन करूँगा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12879)
- **Original**: श्रीमैत्रेयजी बोले-- भगवन्‌ ! मैंने आपसे जो कुछ पूछा था वह सभी आप कह चुके और मैंने भी उसे श्रद्धाभक्तिपूर्वक सुना, अब मुझे और कुछ भी पूछना नहीं है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12880)
- **Original**: हे मुने ! आपकी कृपासे मेरे समस्त सन्देह निवृत्त हो गये और मेरा चित्त निर्म हो गया तथा मुझे संसारकी उत्पत्ति, स्थिति और प्रकूयका ज्ञान हो गया
- **Translation**: 

---

