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

### Verse 1 (Markende Puran 0.1881)
- **Original**: मनुके पुत्र थे। ह0++प्फस्िर4त> रैबत मनुकी उत्पत्ति और उनके मन्यन्तरका वर्णन प्राकंण्डेयजी कहते हैं-- जहा
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1882)
- **Original**: ! पाँचवें नयुका
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1883)
- **Original**: हुआ !' उचर उस दुष्टबुद्धिवाले पुत्र दूसरे तराम रेवत थ्रा। तनको उत्पत्तिका वर्णन करता हूँ,
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1884)
- **Original**: मुनिकुमारक्ती स्त्रीका अपहरण कर लिया। इससे मुतों। पूर्वकालमें ऋतवाकु नामसे प्रसिद्ध एक
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1885)
- **Original**: खिन्नच्चितत होकर ऋतवाकुने कहा--' पनुष्योंका महर्मि थे। उनके बहुत समयतक कोई पत्र गहों
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1886)
- **Original**: बिना पुत्रके रहना अच्छा है; किन्तु कुपुत्नका होना इआ। द्वीर्घ कालके पश्चात्‌ हुआ भी तो रेवती
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1887)
- **Original**: कदापि उत्तम नहों है। कुपुनत्न तो पिक्ता-माताके रक्षत्रके ऑस्तम चरणमें उसका जन्म हुआ।
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1888)
- **Original**: हृदयकों सदा ही सालत्ा रहता है अऔैर स्वर्गमें गये कहोंने बालकक्रे जाठकर्म आदि संस्कार ब्रिधिपूर्वक
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1889)
- **Original**: हुए मितर्रोको भी नरकमें गिरा देता है। बह तो मम्तान्न किय्रे
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1890)
- **Original**: उपनवन आदि भो ऋगाये, किन्तु बह
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1891)
- **Original**: केवल माता -मिन्नाक्ो दुःख देनेके लिये ही होता वृशील ने हो सका। ऊचत्चसे उसका जन्‍्स छुआ,
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1892)
- **Original**: है। ठस पापात्पा पुज्के जन्मकों थिककार है। ?भौसे वे महरँ भी दीवंक्रालव्यायों रेगसे झरत
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1893)
- **Original**: जिनके पत्र सब लोगोंके प्रिय, परोपकारी, शाम्त गे गये / उरी माता भी कोड आदिसे पीड़ित हो
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1894)
- **Original**: त्क उत्तम कर्मोंयें लगे रतनेवाले होते हैं, वे ही धन्त्र हैं मुझे इस जन्ममसें कुंपृत्रके कारण सुख नहीं मिला और परलोकर्स लिगुख होना पड़ा। हुंत दुःख उठाने लगौं। बालकके पित्म जत्वन्त हुख्ली होकर सोचने लगे--'चह़ कैसा अनर्थ प्रात
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1895)
- **Original**: 168 > संक्षिप्त सार्कण्डेगपुराण * 44322:22%%+7 + #&.& 4 220:4 8 1170757 ##% < 7 7:2:3.%*%+00-6
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1896)
- **Original**: +00:2:22.0 70 + 6 & 5 22:87 «5 58 6 20255 «07 & 52: 2207% कुपुत्रका आश्नत्र लेनेत्राल। मेण यह अधम जन्म अपने दोषसे उत्पन्न हुआ है, जो अपनी दुष्टतासे केवल नरकमें ले जानेवाला हैं, उत्तम गत्तिकी हमारे लिये दुःखदायी और बन्धुजनोंके लिये प्राप्ति करानेग्राला तहों।'
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1897)
- **Original**: शोककारक हो गया है? इस प्रकार अल्वन्त (6 पुत्रके दुराचारोंसे। गर्गने कहा--मुनिश्रेष्ठ ! तुम्हारा यह पुत्र रेत्रती ऋतबाकू गुनिक। इृदय जलने लगा। उन्होंने
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1898)
- **Original**: नक्षत्रके अन्तिम चरणमें उत्पन्न हुआ है, अतः 1र्गमुनिसे इसका कारण पूछा दृषित समयमें जन्म ग्रहण करनेके कारण यह दा 22:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1899)
- **Original**: 9 छूजु सुम्हारे लिये दुःखदायों हो गया हैं। (9 ऋतवाक्‌ बोले--मेंर एक ही पृत्र था तो भी तेवती नक्षत्के अन्तिम भागमें उत्पन्न होनेफे कारण इसमें ऐसी दुष्टता आ गयी; इसलिये रेबतौका शीघ्र ही पतन हो जाय। मुनिके इस प्रकार शाप देते हो रेजती नक्ष-्र आकाशसे गिरा। सारा संसार चकितचित्त होकर ग्रह दृश्य देख रहा था। बह नक्षत्र कुमुदगिरिके चारों ओर गिर पड़ा! चहाँके वन, गुफाएँ तथा झरने आदि सहसा उद्भासित हो उठे। रेथर्ती नक्षत्रके गिरनेसे कुमुदगिरिका नाम रैवतक पर्वत
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1900)
- **Original**: हो गया। उस नक्षत्रकी जो कान्ति थी, वह कमलमण्डित सरोवरके रूपमें प्रकट हुईं। उम्र समय उस सरोबरसे एक अत्यन्त सुन्दरी कन्याका 33254. 20: स््क, 4-
- **Translation**: 

---

