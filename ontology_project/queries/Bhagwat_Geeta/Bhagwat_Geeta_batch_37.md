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

### Verse 1 (Bhagwat_Geeta 9.872)
- **Original**: क्षिप्रं भवति धर्मात्मा शश्वच्छान्तिं निगच्छति। कौन्तेय प्रति जानीहि न मे भक्तः प्रणश्यति
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 9.873)
- **Original**: वह शीघ्र ही धर्मात्मा हो जाता है और सदा रहनेवाली परम शान्तिको प्राप्त होता है। हे अर्जुन! तू निश्चयपूर्वक सत्य जान कि मेरा भक्त नष्ट नहीं होता
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 9.874)
- **Original**: मां हि पार्थ व्यपाश्रित्य येउपि स्यु: पापयोनय: । स्त्रियो वैज्यास्तथा शूद्रास्तेडपि यान्ति परां गतिम्‌
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 9.875)
- **Original**: हे अर्जुन! स्त्री, वैश्य, शूद्र तथा पापयोनि-- चाण्डालादि जो कोई भी हों, वे भी मेरे शरण होकर परमगतिको ही प्राप्त होते हैं
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 9.876)
- **Original**: किं पुनर्ब्राह्मणा: पुण्या भक्ता राजर्षयस्तथा। अनित्यमसुखं लोकमिमं प्राप्प भजस्व माम्‌
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 9.877)
- **Original**: फिर इसमें तो कहना ही क्या है, जो पुण्यशील ब्राह्मण तथा राजर्षि भक्तजन मेरी शरण होकर परमगतिको प्राप्त होते हैं। इसलिये तू सुखरहित और क्षणभज्जुर इस मनुष्य शरीरको प्राप्त होकर निरन्तर मेरा ही भजन कर
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 9.878)
- **Original**: मन्मना भव मद्धक्तो मद्याजी मां नमस्कुरु। मामेवैष्यसि युक्‍त्वैवमात्मानं मत्परायण:
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 9.879)
- **Original**: 128 * श्रीमद्धगवद्रीता * मुझमें मनवाला हो, मेरा भक्त बन, मेरा पूजन करनेवाला हो, मुझको प्रणाम कर। इस प्रकार आत्माको मुझमें नियुक्त करके मेरे परायण होकर तू मुझको ही प्राप्त होगा
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 9.880)
- **Original**: 37 तत्सदिति श्रीमद्धगवद्गीतासूपनिषत्सु ब्रह्मविद्यायां योगशास्त्रे श्रीकृष्णार्जुनसंवादे राजविद्याराजगुह्ययोगो नाम नवमोज ध्याय:
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 9.881)
- **Original**: अथ दशमोउ ध्याय: श्रीभयवानुवाच भूय एवं महाबाहो श्रूणु मे परमं वच:। यत्ते5डहं प्रीयमाणाय वश्ष्यामि हितकाम्यया
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 9.882)
- **Original**: श्रीभगवान्‌ बोले--हे महाबाहो ! फिर भी मेरे परम रहस्य और प्रभावयुक्त वचनको सुन, जिसे मैं तुझ अतिशय प्रेम रखनेवालेके लिये हितकी इच्छासे कहूँगा
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 9.883)
- **Original**: न में विदुः सुरगणा: प्रभवं न महर्षयः
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 9.884)
- **Original**: अहमादिहि देवानां महर्षीणां चर सर्वशः
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 9.885)
- **Original**: मेरी उत्पत्तिको अर्थात्‌ लीलासे प्रकट होनेको न देवतालोग जानते हैं और न महर्षिजन ही जानते
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 10.886)
- **Original**: * अध्याय 10* 129 हैं, क्योंकि मैं सब प्रकारसे देवताओंका और महर्षियोंका भी आदिकारण हूँ
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 10.887)
- **Original**: यो मामजमनादिं च वेत्ति लोकमहे श्वरम्‌ । असम्पूढः स मर्त्येषु सर्वपापैः प्रमुच्यते
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 10.888)
- **Original**: जो मुझको अजन्मा अर्थात्‌ वास्तवमें जन्मरहित, अनादि' और लोकोंका महान्‌ ईश्वर तत्त्वसे जानता है, वह मनुष्योंमें ज्ञानवान्‌ पुरुष सम्पूर्ण पापोंसे मुक्त हो जाता है
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 10.889)
- **Original**: बुद्धिज्ञानमसम्मोहः क्षमा सत्यं दम: शम:। सुख दुःखं भवो5 भावो भयं चाभयमेव च
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 10.890)
- **Original**: अहिंसा समता तुष्टिस्तपो दानं यशोउडयशः । भवन्ति भावा भूतानां मत्त एवं पृथग्विधा:
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 10.891)
- **Original**: निश्चय करनेकी शक्ति, यथार्थ ज्ञान, असम्मूढ़ता, क्षमा, सत्य, इन्द्रियोंका वशमें करना, मनका निग्रह तथा सुख-दुःख, उत्पत्ति-प्रलय और भय-अभय तथा अहिंसा, समता, सन्‍्तोष, तप*, दान, कीर्ति और अपकीर्ति--ऐसे ये प्राणियोंके नाना प्रकारके भाव मुझसे ही होते हैं
- **Translation**: 

---

