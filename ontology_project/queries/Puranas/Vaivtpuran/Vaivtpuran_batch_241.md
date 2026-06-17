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

### Verse 1 (Vaivtpuran 13.10962)
- **Original**: श्रीकृष्ण और बलदेव भी कौतूहलवश गोपशिशुओंके स्मरण करके मन-ही-मन सब कुछ जान गये।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10963)
- **Original**: साथ वहाँ प्रत्येक मनोहर स्थानपर बालोचित उन्होंने भीतर-हो-भीतर विचार किया--'यह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10964)
- **Original**: क्रीड़ा करने लगे। नारद! इस प्रकार मैंने नगर- समस्त चराचर जगत श्रीहरिकी इच्छासे ही उत्पन्न
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10965)
- **Original**: निर्माणका सारा वृत्तान्त कह सुनाया। वनमें हुआ है। जिनके भ्रूभज़की लीलामात्रसे ब्रह्मसे गोपबालाओंके लिये जो ग्समण्डल बना था, उसकी लेकर तृणपर्यन्त सारा जगत्‌ आविर्भूत और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10966)
- **Original**: भी बात बतायी। (अध्याय 17) 3 पुष्के च महातीर्थे पुण्याहे देवसंसदि
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10967)
- **Original**: राधाप्रभायप्रस्तावे सुप्रसभेन चेतसा । इदं स्तोत्र महापुण्यं तुभ्य॑दत्त मया मुने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10968)
- **Original**: निन्‍्दकायाबैष्णाय न दातव्य॑ महामुने । यावज्जीवमिदं स्तोत्र त्रिसन्ध्य॑ यः: पठेन्नरः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10969)
- **Original**: राधामाधवयों: पादपओे भक्तिर्भवेदिह । अन्ते. लेत्तयोदास्प॑ शश्वत्सहचरों. भवेत्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10970)
- **Original**: अणिमादिकसिद्धिं. च॒ संप्राप्प तित्यविग्रहम्‌ । ब्रतदानोपवासैश्व सर्वेर्तियमपूर्वकै:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10971)
- **Original**: चतुर्णां चैव वेदानां पाठ: सवर्थिसंयुतै:। सर्वेषा. यज्ञतीर्थानां.. करणैर्विधिबोधिते:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10972)
- **Original**: प्रदक्षिणेने भूमेश्च॒ कृत्साया एव... सप्तधा । शरणागतरक्षायामज्नानां ज्ञानदानत:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10973)
- **Original**: देवानां वैष्णवा्नां च दर्शननापि यत्‌ फलम्‌ । तदेव स्तोत्रपाठस्य कलां नाहति चोडशौम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10974)
- **Original**: स्तोत्रस्यास्‍्य प्रभावेण.. जीवन्मुको.. भवेन्नर:। (17
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10975)
- **Original**: 220--246)
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10976)
- **Original**: + श्रीकृष्णजन्मखण्ड « 489 श्रीवनके समीप यज्ञ करनेवाले ब्राह्मणोंकी पत्रियोंका ग्वालबालोंसहित श्रीकृष्णको भोजन देना तथा उनकी कृपासे गोलोकधामको जाना, श्रीकृष्णकी मायासे निर्मित उनकी छायामयी स्त्रियोंका ब्राह्मणोंके घरोंमें जाना तथा विप्रपत्रियोंके पूर्वजन्मका परिचय नारदजी बोले--मुनिश्रेष्ट! ज्ञानसिन्धो! मैं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10977)
- **Original**: बालकोंके प्रति दयासे भरी हुई हैं। आपका शरणागत शिष्य हूँ। आप मुझे श्रीकृष्ण- श्रीकृष्णजी बात सुनकर वे श्रेष्ठ गोपबालक लीलामृतका पान कराइये। ब्राह्मणोंके सामने जा मस्तक झुकाकर खड़े हो भगवान्‌ श्रीनारायणने कहा--एक दिन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10978)
- **Original**: गये और बोले--'विप्रवरो! हमें शीघ्र भोजन बलरामसहित श्रीकृष्ण ग्वालबालोंको साथ ले
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10979)
- **Original**: दीजिये।' परंतु उनमेंसे कुछ द्विजोंने तो उनकी श्रीमधुवनमें गये, जहाँ यमुनाके किनारे कमल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10980)
- **Original**: बात सुनी ही नहीं और कुछ लोग सुनकर भी खिले हुए थे। उस समय सब बालक सहसोरं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10981)
- **Original**: ज्यों-के-त्यों खड़े रह गये। तब वे पाकशालामें गौओंके साथ वहाँ विचरने और खेलने लगे।
- **Translation**: 

---

