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

### Verse 1 (Vishnu Puran 0.4601)
- **Original**: ज्योतिर्षामा, पृथु, काव्य, चैत्र, अप्नि, लनक और पीवर--ये उस मन्तन्‍्तरके; सप्नर्ति धे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4602)
- **Original**: तथा नर, महाबस्थ्रे पुत्र ही उस समय राज्याधिकारी थे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4603)
- **Original**: हे मैप्रेय ! पाँचवें मन्वन्तरमें रेवत नामक मनु और विधु नामक इन्द्र हुए तथा उस समय जो देवगण हुए उनके नाम सुनो--
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4604)
- **Original**: इस मन्वन्तरमें चौदह-चौदह देवताओंके अमिताभ, भूतरय, चैकुण्ठ और सुमेधा नामक गण थे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4605)
- **Original**: हे विप्र ! इस रैबत-मन्वन्तरमें हिरण्यरोमा, लेदश्री, ऊर्ध्वबाहु, बेदबाहु, सुधामा, पर्जन्य और महासुनि--ये सात सप्तर्तिगण थे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4606)
- **Original**: है सुनिससम ! उस समय रैखतमनुके महातीर्यज्ञाली पुत्र खलबन्धु, सम्भाव्य और सत्यक आदि राजा थे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4607)
- **Original**: हे मैत्रेय ! स्वारोचिष, उत्तम, तामस और रैवत--ये चार मनु, राजा प्रियत्रतके वेशधर कहे जाते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4608)
- **Original**: राजर्षि प्रियब्रतने तपस्याद्वारा भगवान्‌ विष्णुकी आराधना करके अपने व॑दामें उत्पन्न हुए इन चार मन्वन्तराधिपोंको प्राप्त किया था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4609)
- **Original**: छठे मन्वन्तरमें चाश्षुप नामक मनु और मनोजव नामक इन्द्र थे। उस समय जो देवगण थे उनके माम सुतो--
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4610)
- **Original**: उस समय आप्य, प्रसूत, भव्य, पृथक और लेख---ये पाँच प्रकास्के महानुभाव देवगण वर्तमान थे और इममेंसे प्रत्येक गणमें आठ-आठ देवता थे.
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4611)
- **Original**: आ*$1 ] तृतीय अंक 165 सुमेधा विरजाश्रैब ह॒विष्मानुत्तमों मधु: । अतिनामा सहिष्णुश्ष सप्तासन्निति चर्चय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4612)
- **Original**: 28 ऊरु: पृसइशात्ुप्नप्रमुखास्सुमहावल्ठा: । चाक्षुषस्य मनोः पुत्रा: पृथिवीपतयो5भवन्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4613)
- **Original**: 29 विवस्वतस्सुतो विप्र श्राद्धदेवों महाद्युति: । मनुस्संबर्तते धीमान्‌ साम्प्रत॑ सप्मेउन्तरे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4614)
- **Original**: 30 आदित्यबसुरुद्राद्मा देवाक्षात्र महामुने । पुरन्दरस्तथैवात्र मैत्रेय. त्रिदशेश्वर:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4615)
- **Original**: 31 बसिष्ठ: काइयपो5थात्रिर्जमदभिस्सगौतम: । विश्वामित्रभरद्वाजाँ सप्त सप्तर्षयो$भवन्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4616)
- **Original**: 32 इक्ष्वाकुश्न नृगश्चेव धृष्ट: शर्यातिरिव च । नरिष्यन्तश्न विख्यातो नाभागो5रिष्ट एवच
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4617)
- **Original**: 33 करूषश्न॒ पृषध्रश्च सुमहाल्लोकविश्रुत: । मनोर्बेंबस्व॒तस्थैते नव पुत्रा: सुधार्मिका:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4618)
- **Original**: विष्णुशक्तिरनौपम्या सत्तोद्रिक्ता स्थितों स्थिता
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4619)
- **Original**: मन्वत्तरेच्रुदोषेषु देवत्वेनाधितिष्ठति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4620)
- **Original**: 35 अंडोन तस्या जज्ञेजसो बज़स्स्वायम्भुवे5न्तरे । आकूत्यां मानसो देव उत्पन्न: प्रथमेउत्तरे
- **Translation**: 

---

