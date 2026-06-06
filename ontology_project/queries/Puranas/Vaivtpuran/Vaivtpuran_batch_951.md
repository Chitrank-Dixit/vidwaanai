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

### Verse 1 (Vaivtpuran 543.17334)
- **Original**: है। विरहाग्रिसे जली हुई मैं शोकसागरमें डूब ऊँचे आसनपर विराजमान थीं। उस समय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17335)
- **Original**: रही थी। तुमने अपनी पीयूषवर्षिणी दृष्टिसे मेरी मुस्कराती हुई असंख्य गोपियाँ हाथोंमें बेंत लिये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17336)
- **Original**: ओर निहारकर मुझे भलीभाँति अभिषिक्त कर उन्हें घेरे हुए थीं। दिया; जिससे मेरा ताप जाता रहा। तुम्हारे साथ उधर प्राणवल्लभा राधाने भी दूरसे ही
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17337)
- **Original**: रहनेपर मैं शिवा, शिवप्रदा, शिवबीजा और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17338)
- **Original**: + श्रीकृष्णजन्मखण्ड * 767 अडऊक कक क 5 ऋ $ 5 5 अर क अ 5 क इ 5 ऋ # 18 5 अर कक कक 5 5 अ कक 1 5 8 8 5 कक 2 4 5 5 # 5 ऊ कर $ $ $ 5 शक अ अ क अड ऋद अ कड़ा शिवस्वरूपा हूँ; किंतु तुमसे वियुक्त हों जानेपर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17339)
- **Original**: पुष्पोंके मालाजालसे विभूषित एवं चन्दनचर्चित मैं अदृष्ट हो जाती हूँ और मेरी सारी चेट्टाएँ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17340)
- **Original**: पुष्पशय्या तैयार की। वह शय्या एक ऐसे परम नष्ट हो जाती हैं। तुम्हिरे समीप स्थित रहनेपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17341)
- **Original**: मनोहर भवनमें सजायी गयी थी, जिसका निर्माण देह शोभासम्पन्न, पवित्र और सर्वशक्तिस्वरूप
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17342)
- **Original**: बहुमूल्य रत्नोंक सारभागसे हुआ था; श्रेष्ठ मणि, दीखता है; परंतु तुम्हारे चले जानेपर वह शवरूप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17343)
- **Original**: मोती, माणिक्य और हीरोंके हार जिसकी विशेष हो जाता है। नाथ! स्त्री-पुरुषका सामान्य वियोग
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17344)
- **Original**: शोभा बढ़ा रहे थे; कस्तूरी और कुंकुमयुक्त भी अत्यन्त दारुण होता है। यहाँ तो परमात्माके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17345)
- **Original**: वायु जिसे सुगन्धित बना रही थी; जलते हुए वियोगसे पाँचों प्राण शक्तियोंक सहित ही
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17346)
- **Original**: सैकड़ों रलदीपोंसे जो उद्दीत हो रहा था और निकल जाते हैं। नाना प्रकारकी वस्तुओंसे समन्वित धूपोंद्वारा जो यों कहकर देवी राधिकाने परमात्मा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17347)
- **Original**: निरन्तर धूपित रहता था। बहाँ रतिकरी शय्याका श्रीकृष्षको अपने आसनपर बैठाया और हर्षपूर्वक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17348)
- **Original**: निर्माण करके गोपियाँ हँसती हुई चली गयी। उनके चरणोंकी पूजा की। तत्पश्चात्‌ शोभाशाली
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17349)
- **Original**: तब एकान्तमें मकको आकर्षित करनेवाली उस श्रीकृष्ण राधाके साथ रलसिंहासनपर विराजमान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17350)
- **Original**: परम रमणीय शय्याकों देखकर राधा-माधव हुए। उस समय गोपियाँ निरन्तर श्वेत चँंबर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17351)
- **Original**: उसपर विराजमान हुए। उस समय सती राधाने डुलाकर उनकी सेवा कर रही थीं। चन्दनाने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17352)
- **Original**: माधवके गलेमें माला पहनायी, मुखमें सुवासित श्रीहरिके शरीरमें सुगन्धित चन्दनका अनुलेप
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17353)
- **Original**: ताम्बूलका बीड़ा दिया; फिर श्यामसुन्दरके किया। मुस्कराती हुई रतमालाने श्रीहरिके गलेमें
- **Translation**: 

---

