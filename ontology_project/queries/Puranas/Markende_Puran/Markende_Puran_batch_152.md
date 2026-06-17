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

### Verse 1 (Markende Puran 0.3021)
- **Original**: घनुर्ल्यासिहण्टानां नादापूरितदिडुमुखा। निनादैभीषणं:ः काली जिग्ये विस्तारितानना
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3022)
- **Original**: 10 7 तें निमादमुपश्रुत्य दैत्यसैन्यश्चतुर्दिशम्‌। देखी सिंहस्तथा काली सरोषैः परिवारिताः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3023)
- **Original**: आया्ता ब्रह्मण: शक्तिग्रह्माणी साक्रिधीयते
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3024)
- **Original**: माहेश्वरी चृषारूढ ज़िशूलवरधारिणी। 'महाहिवलया प्राप्ता चऋोरेखायिभूषणा।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3025)
- **Original**: कौमारी शक्तिहस्ता ज्ञ मयूरवरवाइना। योद्धुमभ्याययां दैत्यानम्श्िका गुहरूपिणी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3026)
- **Original**: तथष जैष्णवी शक्तिग्गरुडौपरि संस्थिता। शझ्जुच्क्रगदाशार्ड्रखडगहस्ताभ्युपायया
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3027)
- **Original**: यज्ञवाराहमतुल रूर्प या बिप्नतों हरे: शक्ति: साप्यायग्रौ तत्र जाराहीं विभ्रती तनुम
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3028)
- **Original**: भारसिंही नृसिंहस्य जिश्रती सदृर्श बपुः। आप्ता त्त्र सटाक्षेपक्षिप्ततक्षप्रसंह॒ति:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3029)
- **Original**: सज़हस्ता तथ॑वेन्द्रो गजराजोपरि स्थिता। ग्राप्ता सहख्ननयना अथा शक्रस्तथैव सा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3030)
- **Original**: 214 ऋषि कहते हैं--
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3031)
- **Original**: चण्ड और पुण्ड नामक दैत्योंके मारे जाने तथा अहुत-सी सेनाका संहार हो जानेपर दैत्योंके राजा प्रतापी शुम्भके मनमें बड़ा क्रोध हुआ और उसने दैत्योंकी सम्पूर्ण सेनाको युद्धके लिये कूच करनेकी आज्ञा दीं
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3032)
- **Original**: बह बोला--'आज उदायुध नामके छियासी देत्थ-सेनापति अपगी सेनाओंके साथ युद्धके लिये प्रस्थाग करें। कम्बु नामवाले दैत्योंके 2. पा0-स च। 2. पा0--तीश्ादानम्बिका ! 8. पा0--जज्ने बाराह0। 4, 510--तीं। [539 ]स॑0 प्रा0 पु--8
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3033)
- **Original**: 218 #4444# #644 # 44:56 & 4 # 544 6 744:7764 6 चौंरासी सेनानायक अपनी वाहिनीसे घिंरे हुए यात्रा करें
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3034)
- **Original**: पचास कोटिवीर्य-कुलके और सौं
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3035)
- **Original**: धौप्न-कुलके असुर सेनापति मेरो आज्ञासे सेनासहित कूच करें
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3036)
- **Original**: कालक, दौ्ईद, मौर्य और कालकेय असर भी युद्धके लिये तैयार हो मेरों आज्ञासे तुरंत प्रस्थान करें'
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3037)
- **Original**: भवानक शासन करनेवाला असुरगज शुम्भ इस प्रकार आज्ञा दे सहम्नों बड़ी- बड़ी सेनांओकि साथ युद्धके लिये प्रस्थित हुआ
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3038)
- **Original**: उसकी अत्यन्त भयंकर सेना आती देख चण्डिकाने अपने भधनुषकों टंकारसे पृथ्वों और आकाशके बीचका भाग गुँजा दिया
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3039)
- **Original**: राजन्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3040)
- **Original**: तदनन्तर देवीके सिंहने भी बड़े जोर-जोस्से दहाड़ना आरम्भ किया, फिर अम्बिकाने घंटेके शब्दसे उस ध्वनिकों और भो चढ़ा. दिया
- **Translation**: 

---

