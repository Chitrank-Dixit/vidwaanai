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

### Verse 1 (Vaivtpuran 100.18967)
- **Original**: इह लोके सुखं भुक्त्वा लब्ध्वा ज्ञानं निरहननम्‌ । रलबान॑ समारुह्ा गोलोंकंे स॒ च गच्छति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 100.18968)
- **Original**: इति अ्रीब्रह्मवैवते ब्रह्मादिदेवगर्ण: कृत श्रीकृष्णस्तोत्रं सम्पूर्णम्‌ ( श्रीकृष्णजन्मखण्ड 100। 19--33) #आ#ओ10 कप 9क्‍00200 0 सान्दीपनिना तत्पत्या चर कृता श्रीकृष्णस्तुतिः सान्दीपनिरुवाच पर॑ ब्रह्म पर॑ धाम परमीश परात्पर । स्वेच्छामयं स्वयं ज्योतिर्निलिपैको निरड्भुश:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 100.18969)
- **Original**: भक्तैकनाथ भक्तेष्ट. भक्तानुग्रहविग्रह । भक्तवाज्छाकल्पतरो. भक्तानां प्राणवल्लभ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 100.18970)
- **Original**: मायया बालरूपोउसि ब्रहोशशेषवन्दितः: । मायया भुवि भूपालो भुवों भारक्षयाय चा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 100.18971)
- **Original**: योगिनों यं बिदन्येवं ब्रह्मज्योति: सनातनम्‌ । ध्यायन्ते भक्तनिवहा ज्योतिरभ्यन्ते मुदा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 100.18972)
- **Original**: द्विभुज॑ सुरलीहस्तं॑ सुन्दर॑ श्यामरूपकम्‌ । चन्दनोक्षितसर्वाडूं. सस्मित॑ भक्तवत्सलम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 100.18973)
- **Original**: पीताम्बरधरं देव॑ बनमालाविभूषितम्‌ । लीलापाड्डतरड्रैश्ष. निन्दितानड्र.. मूर्च्छितम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 100.18974)
- **Original**: अलक्तभवनं हद्वत्पादपडं. सुशोभनम्‌ । कौस्तुभोद्धासिताड़ूं च दिव्यमूर्ति मनोहरम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 102.18975)
- **Original**: 828 * संक्षिप्त ख्रह्मवैवर्तपुराण « अंक 99% 59% ### 94% ######%### 5 ##### 4 # 4 ###### 4 #########%#ककऋकऋक ईंषद्धास्यप्रसन्न॑ च सुवेषं प्रस्तुतं॑ सुरैः । देवदेव॑ जगन्नाथ जैलोक्यमोहनं॑ परम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 102.18976)
- **Original**: कोटिकन्दर्पलीलाभं कमनीयमनी श्वरम्‌ । अमूल्यरलनिर्माणभूषणौधेन भूषितम्‌। बरं वरेण्यं बरदं बरदानामभीप्सितम्‌।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 102.18977)
- **Original**: बेदानां कारणानां च कारणम्‌ । पाठार्थ मत्प्रियस्थानमागतोइसि च मायया
- **Translation**: 

---

### Verse 12 (Vaivtpuran 102.18978)
- **Original**: पाठं ते लोकशिक्षार्थ रमणं गमन॑ रणप्‌ । स्वात्मारामस्थ च विभो: परिपूर्णतमस्यथ च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 102.18979)
- **Original**: गुरुपल्युवाच अद्य मे सफल जन्म सफल जीवन॑ मम । पातित्रत्य॑ च सफल॑ सफल च॒ तपोवनम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 102.18980)
- **Original**: महक्षहस्तः सफलो दत्त येनान्नमीप्सितम्‌ । मदाशभ्रमस्तीर्थपरस्तीर्थपादपदाद्धित: । तत्पादरजसा पूता गृहाः प्राड्रणमुत्तमम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 102.18981)
- **Original**: यस्य त्वत्पादपदं चैवावयोर्जन्मखण्डनम्‌ । तावद दुःखं च शोकश्न तावद्‌ भोगश्व रोगकः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 102.18982)
- **Original**: तावज्जन्मानि कर्माणि क्षुत्पिपासादिकानि च । यावत्‌ त्वत्पादपद्मस्थ भजन नास्ति दर्शनम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 102.18983)
- **Original**: है कालकाल भगवन्‌ स्त्रष्ट: संहर्तुरीश्ृर। कृपा. कुरू कृपानाथ मायामोहनिकृन्तन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 102.18984)
- **Original**: इति औब्रह्मवैवर्त सान्दीपनिगा तत्पल्या चर कृता अऔीकृष्णस्तुति: सम्पूर्णा। ( श्रीकृष्णजन्मखण्ड 102। 6--21) 3447“ #म्पेस्यिड0-2>->+ भीष्मककृतं श्रीकृष्णस्तोत्रम्‌ भोष्मक उवाच सर्वान्तरात्मा सर्वेषां साक्षी निर्लिप्त एव च। कर्मिणां कर्मणामेव कारणानां च॑ कारणम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 102.18985)
- **Original**: केचिद्‌ बदन्ति त्वामेकं ज्योतीरूपं सनातनम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 102.18986)
- **Original**: केचिच्च परमात्मानं जीवो यत्प्रतिबिम्बक:
- **Translation**: 

---

