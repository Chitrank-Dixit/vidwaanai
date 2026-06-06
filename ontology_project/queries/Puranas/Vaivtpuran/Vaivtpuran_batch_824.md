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

### Verse 1 (Vaivtpuran 543.14794)
- **Original**: असंख्येषू च विश्वेषु॒ ब्रह्मविष्णुशिवात्पक:। स्वरूपायादिबीजाय तदीशविश्वरूपिणे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14795)
- **Original**: नमो गोपाड़ुनेशाय गणेशेश्वररूपिणे । नम: सुरगणेशाय. राधेशाय. नमो. नमः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14796)
- **Original**: राधारमणरूपाय राधारूपधराय च । राधाराध्याय. राधाया: प्राणाधिकतराय च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14797)
- **Original**: राधासाध्याय राधाधिदेवप्रियतमाय च । राधाप्राणाधिदेवाय. विश्वरू्पाय. ते नम:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14798)
- **Original**: बेदस्तुतात्मवेदज्ञरूपिणे बेदिने नमः । वेदाधिष्ठातृदेवाय वेदबीजाय. ते. नमः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14799)
- **Original**: यस्य लोमसु विश्वानि चासंख्यानि चनित्यशः । महद्विष्णोरीश्रराय विश्वेशाय नमो. नमः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14800)
- **Original**: स्वयं प्रकृतिरूपाय प्राकृतायः नमो नमः । प्रकृतीभररूपाय प्रधानपुरुषाय च
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14801)
- **Original**: (70। 56-65)
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14802)
- **Original**: + श्रीकृष्णजन्मखण्ड * 643 कं %#%#################### #####%##########%%%%%%#$%%$%$%$%%%%%% 4; %#######%# करने लगे और बलवती गोपियाँ श्रीकृष्णको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14803)
- **Original**: रथ भूतलपर आया, जो मन्त्रसे प्रेरित होकर गोदमें लेकर चली गयीं। किसी गोपीने क्रोधपूर्वक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14804)
- **Original**: चलता था। वह विचित्र बस्त्रोंसे सुशोभित था। क्रूर अक्रूरको बहुत फटकारा। कुछ गोपियाँ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14805)
- **Original**: श्रीहरिने अपने सामने खड़े हुए उस रथकों देखा। अक्वूरको बस्त्रसे बाँधकर वहाँसे चल दीं। बेचारे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14806)
- **Original**: उसमें श्रेष्ठ मणिरत्र जड़े हुए थे। वह रथ अक्रूरको बड़ा कष्ट प्राप्त हुआ। यह देख माधव [ विश्वकर्माद्वारा बनाया गया था। उसे देखकर राधाके निकट गये और पुनः उन्हें समझाने लगे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14807)
- **Original**: जगदीश्वर श्रीकृष्ण माताके घरमें आये। वहाँ उन्होंने आध्यात्मिक योगद्वारा विगय और आदरके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14808)
- **Original**: भाईसहित भगवान्‌ माधव, जिनके चरणोंकी वन्दना, साथ अक्रूरकों भी समझाया और श्रोराधाको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14809)
- **Original**: मुनीद्ध, देवेन्द्र, ब्रह्म, शिव और शेष आदि करते आश्वासन दिया। इसी समय आकाशसे एक दिव्य
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14810)
- **Original**: हैं, खा-पीकर सुखसे सोये। (अध्याय 70) ><+>#ध्याःषय:00000 शुभ लग्नमें यात्रासम्बन्धी मड्गलकृत्य करके श्रीकृष्णका मथुरापुरीको प्रस्थान, पुरीकी शोभाका वर्णन, कुब्जापर कृपा, मालीको वरदान, धोबीका उद्धार, कुब्जाका गोलोकगमंन, कंसका दुःस्वप्न, रड्ढरभूमिमें कंसका पधारना, धनुर्भड़्, हाथीका वध, कंसका उद्धार, उग्रसेनको राज्यदान, म्राता-पिताके बन्धन काटना, वसुदेवजीद्वारा नन्‍्द आदिका सत्कार और ब्राह्मणोंको दान श्रीनारायण कहते हैं--नारद! जब वायुसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14811)
- **Original**: पल्लवसे युक्त भरा हुआ कलश रखा गया। दाहिने सुवासित, चन्दननिर्मित और फूलोंसे बिछी हुई
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14812)
- **Original**: भागमें प्रज्वलित अग्नि तथा ब्राह्मणदेवता उपस्थित शब्यापर राधिकाजी सो गयीं तथा गोपिकाएँ भी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14813)
- **Original**: हुए। सामने पति-पुत्रवती सती साध्वी स्त्री, गाढ़ निद्रामें निमग्र हो गयीं, तब रातमें तीसरे
- **Translation**: 

---

