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

### Verse 1 (Vishnu Puran 0.10961)
- **Original**: 9 छन्न॑ यत्सलिलस्रावि तज्हार प्रचेतस: । मन्दरस्य तथा श्ूड़़े हतवान्मणिपर्वतम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10962)
- **Original**: 10 अपृतस्नाविणी दिव्ये मन्मातुः कृष्ण कुण्डले । जहार सोउसुरो5दित्या वाउछत्यैरावत गजम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10963)
- **Original**: 11 दुर्नीतमेतद्ोविन्द मया तस्य निवेदितम्‌। यदत्र प्रति कर्तव्यं तत्स्वय॑ परिपृइ्यताम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10964)
- **Original**: 12 श्रीपएाशर उबाच इति श्रुत्वा स्मितं कृत्वा भगवान्देवकीसुत: । गृहीत्वा बासखं हस्ते समुत्तस्थो वरासनात्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10965)
- **Original**: 13 सश्लित्यागतमारुदह्दा गरुडे गगनेचरप्‌ । सत्यभामां समारोप्य ययौ प्राग्ज्योतिष पुरम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10966)
- **Original**: 14 आरुह्नौरावतं नाग शक्रो5पि त्रिदिवं ययो । ततो जगाम कृष्णश्न पश्यतां द्वारकौकसाम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10967)
- **Original**: 15 प्राग्ज्योतिषपुरस्थापि समन्ताच्छतयोजनम्‌ । आचिता मौरबैः पाशै: क्षुरान्तैर्भूद्विजोत्तम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10968)
- **Original**: 16 तांश्िच्छेद हरिः पाश्ञान्क्षिप्या चक्र सुदर्शनम्‌। ततो मुरस्समुत्तस्थो त॑ जघान च केशव:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10969)
- **Original**: 17 मुरस्य तनयान्सप्त सहस््रांस्तांस्ततो हरिः । चक्रधारामिनिर्दग्धांशधकार झलभानिव
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10970)
- **Original**: 18 हत्वा मुरं हयग्रीज॑ तथा पश्चजनं ट्विज
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10971)
- **Original**: प्राग्ज्योतिषपुरं धीमांस्त्वराबान्समुपाद्रबत्‌ । 19 नरकेणास्यथ॒तत्राभून्यहासैन्येन संयुगम्‌। कृष्णस्य यत्र गोविन्दो जन्ने दैत्यान्सहल्नश:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10972)
- **Original**: 20 शस्त्राख्रवर्ष मुझन्तं त॑ भौम॑ नरक बली। क्षिप्त्वा चक्र द्विधा चक्रे चक्री दैतेयत्रक्रहा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10973)
- **Original**: 29 हते तु नरके भूमिर्गृहीत्वादितिकुण्डले । उपतस्थे जगन्नाथ वाक्य चेदमथाब्रवीत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10974)
- **Original**: 22 श्रीविष्णुपुराण [ अ0 29 है शक़दमन! यह पृथिवीका पुत्र नरकासुर प्राग्ज्योतिषपुरका स्वामी है; इस समय यह सम्पूर्ण जीवोंका घात कर रहा है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10975)
- **Original**: है जनार्दन । उसने देवता, सिद्ध, असुर और राजा आदिकोंकी कन्याओंको बल्मत्‌ स्खकर अपने अन्तःपुरमें बन्द कर रखा है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10976)
- **Original**: इस दैत्यने वरुणका जल बरसानेवाला छत्र और मन्दगाचलका मणिपर्वत नामक शिखर भी हर लिया है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10977)
- **Original**: है कृष्ण ! उसने मेरी माता अदितिके अमृतस्लावी दोनों दिव्य कुण्डल ले लिये हैं और अब इस ऐराबत हाथीको भी लेना चाहता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10978)
- **Original**: हे गोविन्द ! मैने आपको उसकी ये सब अनीतियाँ सुता दी हैं; इनका जो प्रतीकार झोना चाहिये, बह आप स्वयं विचार लेँ”
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10979)
- **Original**: श्रीपराहरजी बोले--इन्द्रके ये बचन सुनकर श्रीदेवकीनन्दन मुसकाये और इन्द्रका हाथ फ्कड़कर अपने ओह आसनसे उठे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10980)
- **Original**: फिर स्मरण करते ही उपस्थित हुए आकाशगामी गरुडपर सत्यभामाको चढ़ाकर स्वयं चढ़े और प्राग्ज्योतिषपुरको चले
- **Translation**: 

---

