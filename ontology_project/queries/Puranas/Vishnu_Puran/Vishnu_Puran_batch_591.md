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

### Verse 1 (Vishnu Puran 0.11801)
- **Original**: 9 नातिक़ान्तुमलं ब्रहांस्तदद्यापि महोदधि: । नित्य सन्निहितस्तत्र भगवान्केशवों यतः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11802)
- **Original**: 10 श्रीपराशरजी बोले-- अर्जुनने राम और कृष्ण तथा अन्यान्य मुख्य-मुख्य यादवोके मृत देहोंकी स्व्रोज कराकर क्रमशः उन सबके ऑऔर्ध्यदैह्विक संस्कार किये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11803)
- **Original**: भगवान्‌ कृष्णकी जो रुक्मिणी आदि आठ पटरानी बतलायी गयी हैं उन सबने उनके शरीरका आलिज्ञन कर अग्निमें प्रवेश किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11804)
- **Original**: सती रेबतीजी भी बलरामजीके देहका आलिंगन कर, उनके अंग-संगके आह्वादसे शीतल प्रतीत होती हुई प्रज्वल्ित अग्निमें प्रवेश ऋर गयीं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11805)
- **Original**: इस सम्पूर्ण अनिष्टका समाचार सुनते हो उपग्रसेन, बसुदेव, देवकी और रोहिणीने भी अप्रिमें प्रवेदा किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11806)
- **Original**: तदनन्तर अर्जुन उन सबका विधिपूर्वक प्रेत-कर्म कर बज तथा अन्यान्य कुटुम्बियोंको साथ केकर द्वारकासे बाहर आये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11807)
- **Original**: द्वारकासे निकली हुई कृष्णचन्द्रको सहस्ननों पत्नियों तथा बज और अम्यान्य बान्धवोंको [ सावधानतापूर्वक ] रक्षा करते हुए अर्जुन धीरे-धीरे चले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11808)
- **Original**: हे मैत्रेय ! कृष्णचन्द्रके मर्ल्यलोकक त्याग करते ही सुधर्मा सभा और पारिजात-वृक्ष भी स्वर्गल्मेकको चले गये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11809)
- **Original**: जिस दिन भगवान्‌ पृथिवोकों छोड़कर स्वर्ग सिधारे थे ठसी दिनसे यह मल्विनदेह महाबली कलियुग पृथिवीपर आ गया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11810)
- **Original**: इस प्रकार जनशून्य द्वास्काको समुद्रने डखों दिया, केवल एक कृष्णचनत्द्रके अवनको वह नहीं डुबता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11811)
- **Original**: हे क्रहमन्‌! उसे डुबानेमें समुद्र आज भी समर्थ नहीं है क्योंकि उसमें भगवान्‌ कण्णचन्द्र सर्वदा निवास करते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11812)
- **Original**: 4916 तदतीव महापुण्यं सर्वपातकनाशनम्‌ । विष्णुश्रियान्बितं स्थान दृष्ठा पापाद्विपुच्यते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11813)
- **Original**: 11 पार्थ: पदञ्ननदे देशे बहुधान्यधनान्यिते। चकार बासं सर्वस्थ जनस्य मुनिसत्तम:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11814)
- **Original**: 12 ततो लोभस्समभवत्पार्थेनेकेन धन्विना । दृष्ठा ख्रियो नीयमाना दस्पूनां निहतेश्वरा:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11815)
- **Original**: 13 ततस्ते पापकर्माणो लोभोपइतचेतस: । आभीरा मन्त्रवामासुस्समेत्यात्यन्तदुर्णदा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11816)
- **Original**: 14 अयमेको3र्जुनो धन्वी खत्रीजनं निहतेश्वरम्‌। नयत्यस्मानतिक्रम्य धिगेतद्धवतां बलम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11817)
- **Original**: 15 हत्या गर्वसमारूढो भीष्मद्रेणजयद्रथान्‌। कर्णादीश्व न जानाति बलें ग्रामनिवासिनाम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11818)
- **Original**: 16 यहष्टिहस्तानवेक्ष्यास्मान्थनुष्पाणिस्स दुर्मति: । स्बनिवावजानाति कि वो बाहुभिरुक्नते:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11819)
- **Original**: 97 सहस्लहो5भ्यभ्रावन्त ते जन॑ निहतेश्वरम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11820)
- **Original**: 18 ततो निर्भ्स्य कौन्तेय: प्राह्मभीरान्हसत्रिव । निवर्तध्वमधर्मज्ञा यदि न स्थ मुमूर्षव:
- **Translation**: 

---

