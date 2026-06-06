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

### Verse 1 (Markende Puran 0.3041)
- **Original**: धनुषकों टंकार, स्रिंहकी दहाड़ और मंटेक़ी ध्वनिसे सम्पूर्ण दिशाएँ गुँज डरठीं। उस भयंकर शब्दसे कालीने अपने बिकराल मुखकों और भी बढ़ा लिया हथा इस प्रकार ले विजयिनी हुईं
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3042)
- **Original**: उस तुमुल नादको सुनकर दुत्योंकी सेनाओंने चार्ये ओर्से आकर मभण्डिकादेवो, सिंह उथा कालीदेवीको क्रोधपूर्वक बेर लिया
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3043)
- **Original**: इसी बीचमें असुरोंके विनाश तथा देवताओंके अभ्युदयके लिये ब्रह्मा, शिव, कॉर्पिकेय, विष्णु तथा इन्द्र आदि देब्रोंकी शक्तियाँ, जो अत्वन्त पराक्रम और बलसेे सम्मन्न थीं, उनके शरीरॉसे निकलऋर उन्हींके रूपमें अण्ड्िकादेवीके पाम्त गर्यी
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3044)
- **Original**: 8152-13
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3045)
- **Original**: जिस देखताका जैसा रूप, जैसी वेश भ्रूषा और जैसा बाहर है, ठीक वैसे हों साभनोंसे सम्पन्न हो ठउस्तकौ कझृक्ति असरोंसे युद्ध ऋरनेके लिये आयी।
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3046)
- **Original**: सबसे पहले हंसयुक्त विमानपर बेठी हुई अक्षसूत्र और कमण्डलुसे मुशोभित ब्रह्माजीकी शक्ति उपस्थित हुई, जिसे ब्रह्माणी कहते हैं
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3047)
- **Original**: महादेवजीको शक्ति + संक्षिप्त मार्कण्डेच्रपुराण * चृषभपर आऊरूद्द हो ह्ाथोंपें श्रेष्ठ त्रिशुल धारण किये महानागका कछ्लुण पहने, मस्तकमें चन्द्ररेख्रासे निभूषित हों वहाँ आ पहुँची
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3048)
- **Original**: रूप धारण क्रिये श्रेष्ठ मयूरपर आरूढ़ हो हाथपमें
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3049)
- **Original**: शक्ति लिये दैत्वोंसे युद्ध करनेके लिये आयों
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3050)
- **Original**: इसी प्रकार भगबान्‌ विष्णुकों शक्ति गरुड़पर विराजमान हो शह्लु, चंक्र, गदा, शाज्जधनुष तथा खड़े हाथमें लिये वहाँ आयी
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3051)
- **Original**: अनुपम गज्ञवाराहका रूप धारण करनेत्नाले श्रोहरिकी जो शक्ति हैं, वह भी वाराह शरीर धारण करके वहाँ उपस्थित हुईं
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3052)
- **Original**: नारसिंही शक्ति भी नृसिंहके समान शरीर धारण करके वहाँ आयी। उसकी गर्दनके बालोंके झटकेसे आकाशके तारे सिंखरे पड़ते थे
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3053)
- **Original**: इसी प्रकार इन्द्रकी शक्ति बग् हाथमें लिये गजराज ऐराबतपर बैठकर आयी। उसके भी सहस्र नेत्र थे। इन्द्रका जैसा रूप हैं, वैसा हीं उसका भी था
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3054)
- **Original**: कार्तिकेयजीकी शक्तिरूपा ज़गदम्बिका उन्हींका
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3055)
- **Original**: + रक्तबीज-वध् + 219 .+5%&&###&#& # # 4 * # 44477 + 3414 607 07707 7 क 017 1430 7737:33.335.7:3.:2:::553.:05.77:0:77:5 त्ततः परिवृतस्ताभिरीशानों देवशक्तिभि:।
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3056)
- **Original**: चण्डाइहासैरसुरा:. शिवदूत्यभिदृषिताः
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3057)
- **Original**: इन्यन्तामसुरा: शीघ्र प्रम प्रीत्या55ह त्ण्डिकाम्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3058)
- **Original**: पेतु: पृथिव्यां पत्तितांस्तांश्रआदाध सा तदा
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3059)
- **Original**: ततो देवीशरीरात़ु विनिष्क्राज्तातिभीषणा। तदनन्दर उन देब-शक्तियोंसे धि! 65 महादेवजोने चअण्डिकाशक्तिरत्युप्रा शिवाशतनिनादिनी
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3060)
- **Original**: चण्डिकासे कहा--' मेरी प्रम्नअ्ताके लिये तुम सा चाह धुूम्रजटिलमीशानमपराजित्ता। शीघ्र ही इन असुरोंका म्ंह।र करो!
- **Translation**: 

---

