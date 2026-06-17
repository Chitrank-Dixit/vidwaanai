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

### Verse 1 (Vaivtpuran 543.14774)
- **Original**: प्रतिष्ठारहितको प्रतिष्ठाकी प्राप्ति होती है और जो ब्रह्माण्ड नित्य निवास करते हैं, उन महाविष्णुके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14775)
- **Original**: यशस्वी नहीं है, वह भी अनायास ही महान्‌ ईश्वर आप विश्वेश्वरको बारंबार नमस्कार है। आप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14776)
- **Original**: यश प्राप्त कर लेता है। स्वयं ही प्रकृतिरूप और प्राकृत पदार्थ हैं।। तदनन्तर अक्रूरजी रातके समय अत्यन्त प्रकृतिके ईश्वर तथा प्रधान पुरुष भी आप ही
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14777)
- **Original**: प्रसन्नचित्त हो रमणीय चम्पाकी शब्यापर श्रीकृष्णको हैं। आपको बारंबार नमस्कार है*। छातीसे लगाकर सोये। प्रातःकाल सहसा उठकर इस प्रकार स्तुति करके अक्रूरजी नन्दरायजीके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14778)
- **Original**: परम उत्तम आहिक कृत्यका सम्पादन करके सभाभवनमें मूच्छित हो गये और सहसा भूमिपर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14779)
- **Original**: उन्होंने जगदीश्वर श्रीकृष्ण तथा बलरामकों अपने गिर पड़े। उसी अवस्थामें पुनः उन्होंने अपने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14780)
- **Original**: रथपर बिठाया। पाँच प्रकारके गव्य (दूध, दही, हृदयमें और बाहर भी सब ओर उन श्यामसुन्दर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14781)
- **Original**: माखन, घी और छाँछ) तथा नाना प्रकारके परम सर्वेश्वर परमात्माको देखा। वे ही विश्वमें व्याप्त दुर्लभ द्रव्य रखवाये। बृषभानु, नन्द, सुनन्‍्द तथा थे और वे ही विश्वरूपमें प्रकट हुए थे। नारद!
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14782)
- **Original**: चन्द्रभानु गोपकों भी साथ ले लिया। उस समय अक्रूरजीको मूर्च्छित हुआ देख नन्दजीने आदसरपूर्वक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14783)
- **Original**: ब्रजराज नन्‍्द गोपने आनन्दमग्न हो नाना प्रकारके उठाया और रमणीय रत्नसिंहासनपर बिठा दिया।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14784)
- **Original**: बाद्य-मृदड्भ, मुरज (ढोल), पटह, पणव, ढक्ा, तत्पश्षात्‌ उन्होंने अक्रूरसे सारा वृत्तान्त पूछा और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14785)
- **Original**: दुन्दुभि, आनक, सज्जा, संनहनी, कांस्य-पट्ट बारंबार कुशलप्रश्न करते हुए उन्हें मिष्टान्न भोजन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14786)
- **Original**: (झाँझ), मर्दल और मण्डवी आदि बजवाये। कराया। अक्रूरने कंसका सारा वृत्तान्त कह सुनाया
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14787)
- **Original**: बाजोंकी ध्वनि और बलराम तथा श्रीकृष्णके और यह भी कहा कि अपने माता-पिताको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14788)
- **Original**: जानेका समाचार सुन श्रीकृष्णको रथपर बैठे देख बन्धनसे छुड़ानेके लिये बलराम और श्रीकृष्णको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14789)
- **Original**: गोपियाँ प्रणय-कोपसे पीड़ित हो उनके पास आ वहाँ अवश्य चलना चाहिये। पहुँचीं। ब्रह्मन्‌! श्रीकृष्फे मना करनेपर भी जो अक्रूरद्धारा किये गये इस स्तोत्रका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14790)
- **Original**: श्रीराधाकी प्रेरणासे उन गोपकिशोरियोंने पैरोंके एकाग्रचित्त होकर पाठ करता है, वह पुत्रहीन आघातसे राजा कंसके उस रथको अनायास ही हो तो पुत्र पाता है और भार्याहीन हो तो उसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14791)
- **Original**: तोड़ डाला। उसपर बैठे हुए सब गोप हाहाकार * नमः कारणरूपाय परमात्मस्वरूपिणे । सर्वेधामपि. विश्वानामीश्वराय. नमो. नमः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14792)
- **Original**: पराय प्रकृतेरीश परात्पतराय. च । निर्युणायः निरीहाय नौरूपाय_ स्वरूपिणे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14793)
- **Original**: सर्वदेवस्वरूपाय सर्वदेवे श्रराय च । सर्वदेवाधिदेवाय विश्वादिभूतरूपिणे
- **Translation**: 

---

