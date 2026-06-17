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

### Verse 1 (Vishnu Puran 0.3981)
- **Original**: होती है ?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3982)
- **Original**: यदि सातों गणोंका यह यृष्टि आदि कार्य विवस्वानुदितो मध्ये यात्यस्तमिति कि जन: । समान ही है तो सूर्य उदय हुआ, अब मध्यमें है, अब अस्त होता है' ऐसा त्लोग क्यों कहते हैं 7
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3983)
- **Original**: ब्रवीत्येतत्सम॑ कर्म यदि सप्तगणस्थ तत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3984)
- **Original**: . पराझरजी घोले--हे मैत्रेय जो कुछ तुमने पूछा मैत्रे ऑफ्राशर उवाच । है उसका उत्तर सुनो, सूर्य सात गणोमेंसे ही एक श्रूयतामेतद्यद्धवान्परिपृच्छति हैं तथापि उम्रमें प्रधान होनेसे उनकी विश्लेषता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3985)
- **Original**: यथा सप्तगणेउप्येक: प्राधान्येनाधिकों रति:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3986)
- **Original**: 6 भगवान्‌ किष्णुकी जो सर्वशक्तिमयी ऋक्‌, यगजुः, सर्वशक्ति: परा बिष्णोर्क्रम्यजुःसामसंज्ञिता । साम नामकी परा ज्ञक्ति है वह वेदत्रयी ही सूर्यको ताप सैषा त्रयी तपत्यंहो जगतश्न हिनस्ति या
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3987)
- **Original**: अदान करती है और [उपासना किये जानेपर] संसारके से विष्णु: स्थित: स्थित्यां जगतः पालनोद्यतः । समस्त पार्पोको नष्ट कर देती है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3988)
- **Original**: हे द्विज ! जगतकी ऋग्यजुःसामभूतोउन्तः सबितु्विन तिष्ठति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3989)
- **Original**: । 8 स्थिति और पालनके लिये वे ऋक्‌, यजु: और सामरूप मासि मासि अंतर के दे सो दस । विष्णु सूर्यके भीतर निवास करते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3990)
- **Original**: प्रत्येक मासमें रवियों बै जो-जो सूर्य होता है उसी-उसीमें वह वेदज़यीरूपिणी त्रयीमबी विष्णुञ्ाक्तिरवस्थान॑ करोति वै
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3991)
- **Original**: 9 विष्णुकी परा शक्ति निवास बरती है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3992)
- **Original**: पूर्वाहमें ऋक्‌, ऋत्त: स्तुवन्ति पूर्वाह्नि मध्याद्लेडथ यजूंषि वे । मध्याहमें यहद्रथन्तरादि यजुः तथा सायेकालयों बुहृद्रथन्तरादीनि सामान्यद्डः क्षये रविम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3993)
- **Original**: सामश्रुतियाँ सूर्यकी स्तुति करती है *
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3994)
- **Original**: 10 । + इस विषयमें यह श्रुति भी है-- ड़ कफ! “ऋच: पूर्वाद्ि दिवि देव ईयते यजुर्वेदे तिष्ठति मध्ये अह्: समसकेदेनास्तमये महीयते ।'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3995)
- **Original**: शेर झश्रीविष्यापुराण आ* 11 अड्जमेषा श्रयी बिष्णोर्ऋग्यजुःसामसंज्ञिता । विष्णुशक्तिरवस्थानं सदादित्ये करोति सा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3996)
- **Original**: 11 न केबल रखे: शाक्तिवैंप्णवी सा अयीमयी । ब्रह्मयाथ पुरुषों रुद्रस्नयमेतत्रयीमयम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3997)
- **Original**: 12 र्द्ध: साममयोउन्ताय तस्मात्तस्याशुचिध्यनि:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3998)
- **Original**: 13 एवं सा सात्विकी शक्तिवैंश्णवी या श्रवीमयी । आत्मसप्तगणस्थ त॑ भास्वन्तमधितिष्ठति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3999)
- **Original**: 94 तया चाधिष्ठितः सो5पि जाज्वलीति स्वरश्मिभि: । तमः समस्तजगतां नाशं॑ नयति चास्बिलम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4000)
- **Original**: 15 स्तुबन्ति चैनें मुनयो गन्धर्वैर्गीयते पुरः। नृत्यन््यो5प्सरसो यान्ति तस्थ चानु निशाचरा:
- **Translation**: 

---

