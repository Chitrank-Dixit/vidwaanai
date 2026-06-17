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

### Verse 1 (Vaivtpuran 102.18987)
- **Original**: केचित्‌ प्राकृतिकं जीव॑ सगुण श्रान्तबुद्धय:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 102.18988)
- **Original**: केचित्रित्पशरीर॑ च॒ बुद्धाश्व॒ सूक्ष्मबुद्धय:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 102.18989)
- **Original**: ज्योतिरभ्यन्ते नित्य देहरूप सनातनम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 102.18990)
- **Original**: कस्मात्तेज: प्रभवति साकारमीश्वरं विना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 102.18991)
- **Original**: एवं स्तुत्या स बाचान्तः स्मरन्‌ विष्णुं च नारद। पाद्यं पद्मार्थिते पादपद्ये चायं ददौ मुदा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 102.18992)
- **Original**: इति औब्रह्मवैवर्ते भ्रीष्मककृतं औ्रीकृष्णस्तोत्रं सप्पूर्णय्‌। (श्रीकृष्णजन्मखण्ड 107। 88--92) >3/0008> पक यक0002000000 दुर्वासःकृतं श्रीकृष्णस्तोत्रम्‌ दुर्वासा उवाच जय जय जगतां नाथ जितसर्व जनार्दन सर्वात्मक सर्वेश सर्वबीज पुरातन निर्गुण निरीह निर्लिप्त निरक्षन निराकार भक्तानुग्रहविग्रह सत्यस्वरूप सनातन निःस्वरूप नित्यनूतन ब्रहोशशेषधनेशबन्दित पद्मया सेवितपादपश ब्रह्मस्योतिरनिर्वच्चनीय वेदाविदितगुणरूप महाकाशसम्माननीय परमात्मन्नमो स्तु ते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 102.18993)
- **Original**: इत्येवमुक्ला मनसा हरेरनुपतेन च। प्रणम्य तस्थौ विप्रेन्द्रस्तत्रैव पुरतो हरेः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 102.18994)
- **Original**: तमुबाच॒ जगजन्नाथों हित॑ सत्य पुरातनम्‌। ज्ञानं च बेदविहित सर्वेधां च सतां मतम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 102.18995)
- **Original**: इति श्रीब्रह्मवैवरतें दुर्वास: कृत श्रीकृष्णस्तोजरं सम्पूर्ण । ... ( श्रीकृष्णजन्मखण्ड 112। 51-53)
- **Translation**: 

---

### Verse 10 (Vaivtpuran 113.18996)
- **Original**: » श्रीकृष्यास्तोत्राणि « <29 शिशुपालस्य जीवात्मना कृतं अश्रीकृष्णस्तोज्रम्‌ शिशुपाल उवाच खेदानां जनकोउसि त्वं बेदाड़ानां च माधव
- **Translation**: 

---

### Verse 11 (Vaivtpuran 113.18997)
- **Original**: सुराणामसुराणां च॒ प्राकृतानां च देहिनाम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 113.18998)
- **Original**: सुक्ष्मं विधाय सृष्टिक्ष कल्पभेद॑ करोषि च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 113.18999)
- **Original**: मायया च्व स्वयं ब्रह्मा शंकर: शेष एब च
- **Translation**: 

---

### Verse 14 (Vaivtpuran 113.19000)
- **Original**: मनबवो मुनयक्षैव वेदाश्न॒ सृष्टिपालका: । कलांशेनाप कलया दिकक्‍्पालाश्व॒ ग्रहादय:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 113.19001)
- **Original**: स्वयं पुमान्‌ स्वयं स्त्री च॒ स्वयमेव नपुंसकः । कारणं च स्वयं कार्य जन्यश्न जनकः स्वयम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 113.19002)
- **Original**: यत्रस्य च गुणों दोषो यन्त्रिणश्न श्रुतौ श्रुतम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 113.19003)
- **Original**: सर्वे यन्त्रा भवान्‌ यन्त्री त्वयि सर्व प्रतिष्ठितम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 113.19004)
- **Original**: मम क्षमस्वापराध॑ मूढस्थ द्वारिणस्तब । ब्रह्मशापात्‌ कुबुद्धेश्व रक्ष रक्ष जगदगुरो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 113.19005)
- **Original**: इति श्रीब्रह्मवैवर्ते शिज्ुपालस्य जीवात्पना कृत॑ श्रीकृष्णस्तोत्रं सम्पूर्णय्‌। ( श्रीकृष्णजन्मखण्ड 113। 28-33) #01/0*- की पिलय204.2,5002 बलिकृतं श्रीकृष्णस्तोत्रम्‌ बलिरुवाच अदित्या: प्रार्थननेव मातुर्देव्या ख़तेन च । पुरा वामनरूपेण त्वयाहं सनद्धचितः प्रभो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 113.19006)
- **Original**: सम्पद्रूषा महालक्ष्मीर्दत्ता भक्ताय भक्तितः । शक्राय मत्तो भ्क्ताय क्षात्रे पुण्यवते ध्रुबम्‌
- **Translation**: 

---

