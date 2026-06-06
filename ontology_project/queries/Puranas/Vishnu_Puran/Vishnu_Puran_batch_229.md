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

### Verse 1 (Vishnu Puran 0.4561)
- **Original**: 5 स्वायम्भुवो मनुः पूर्व पर: स्वारोचिषस्तथा । उत्तमस्तामसश्लैव रैवतश्लाक्षपस्तथा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4562)
- **Original**: 6 बड़ेते मनवो5तीतास्साम्परत॑ तु रवेस्सुतः। वैबस्वतो5यं यस्वैतत्सप्तम॑ वर्ततेउन्तरम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4563)
- **Original**: 7 स्वायम्भुवं तु कथित कल्पादावन्तरं मया । देवास्सप्तर्षपश्चेथष यधावत्कधिता मया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4564)
- **Original**: 8 अत ऊर्थ्व॑ प्रवक्ष्यामि मनोस्स्वारोचिषस्य तु । मन्वन्तराधिपान्सम्यग्देवर्षस्तत्सुतांस्सथा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4565)
- **Original**: 9 पारावतास्सतुषिता देबास्स्वारोचिषेउन्तरे । विपक्षित्तत्र देवेडओोि प्रैत्नेयासी्महाखत्ठ:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4566)
- **Original**: 10 ऊर्ज: स्ता्भस्तथा प्राणो वातो5थ पृषभस्तथा । निस्यञ्र परीयांश्र तत्र सप्तर्षवोईभवन्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4567)
- **Original**: 11 चैत्रकिम्पुरुषाद्याश्च सुतास्स्वारोचिषस्यथ तु । द्वितीयमेतद्याख्यातमन्तरं श्रूणू चोत्तमम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4568)
- **Original**: श्रीमैत्रेयजी खोले--हे गुर्देव ! आपने पृथिवी और समुद्र आदिकी स्थिति तथा सूर्य आदि ग्रहगणके संस्थानका मुझसे भल्म्रे प्रकार अति विस्तारपूर्वक वर्णन किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4569)
- **Original**: आपने देवता आदि और ऋषिगणोंकी सृष्टि तथा चातुर्वर्ण्य एवं तिर्यक्‌-योनिगत जीवॉकी उत्पत्तिका भो ज्र्णन किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4570)
- **Original**: श्रुय और प्रह्ादके घरित्रोंको भी आपने विस्तारपूर्वक सुना दिया। अतः हे गुरो ! अब मैं आपके मुखारविन्दसे सम्पूर्ण मन्वन्तर तथा इन्द्र और देवनाओंके सहित मन्वत्तरोंके अधिपति समस्त मनुओँंका यर्णन सुनना चाहठ हूँ [ आप बर्णन कोजिये]
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4571)
- **Original**: श्रीपरादारजी खोले--भूतकालूमें जितने मन्वन्तर हुए हैं तथा आगे भी जो जो होंगे, उप सबका मैं तुमसे क्रमद्ञा: वर्णन करता हूँ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4572)
- **Original**: प्रथम मनु स्वायम्मुव थे। उनके अन्तर क्रमशः स्वारोचिष, उत्तम, तामस, रेखत और चाश्षुष हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4573)
- **Original**: ये छः मनु पूर्वकालमें हो चुके हैं । इस समय सूर्यपुत्र वैबस्वत मनु हैं, जिनका यह सातवाँ मन्ब्ननर वर्तमान है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4574)
- **Original**: कल्पके आदिमें जिस स्वायम्थुब-मन्वत्तस्के पिपयमें मैंने कहा है उसके देखता और सप्तर्पियोका तो मैं पहले ही यथावत्‌ वर्णन कर चुका हूँ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4575)
- **Original**: अब आगे में स्वारोचिष मनुके सन्वन्तराधिकारी देखता, ऋषि और मन्‌पुशेका स्पष्टतया तर्णन करूँगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4576)
- **Original**: हे मैत्रेय ! खारोचिषमन्वन्तरमें पारावत और तुषितगण देवता थे महाबली विपक्षित्‌ देखराज इन्द्र थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4577)
- **Original**: कर्ज, स्तम्भ, प्राण, खात, पृषभ, निरय और परीवान्‌--ये उस समय सप्तति थे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4578)
- **Original**: तथा चैत्र और किम्पुरुष आदि स्वारोचिपसनूके पुत्र थे। इस प्रकार सुमसे द्वितीय ममब्तस्का वर्णन कर दिया। अब उत्तम-मन्वन्तरका खिखरण सुनो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4579)
- **Original**: श्द्चश बिष्णुपुराण (अः 9 तृतीयरेउप्यन्तरे ब्रह्मन्नुत्तमो नाम यो मनुः। सुशान्तिर्नाम देकेन्द्रो मैत्रेयासीत्सुरेश्वरः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4580)
- **Original**: 14 सुधामानस्तथा सत्या जपाश्चाथ प्रतर्दनाः । वशवर्तिनश् पञ्नैते गणा द्वादशकास्स्मृता:
- **Translation**: 

---

