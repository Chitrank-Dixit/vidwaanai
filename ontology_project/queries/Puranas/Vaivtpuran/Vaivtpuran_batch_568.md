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

### Verse 1 (Vaivtpuran 43.18012)
- **Original**: कारणे सर्वसिद्धीनां सिद्धेश्वरि प्रसीद मे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 43.18013)
- **Original**: ज्ञने यदुक्त तत्सव॑ क्षमस्व परमेश्वारि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 43.18014)
- **Original**: केचित्तत्र मतद्वैधे व्याख्याभेद॑ विदुर्वुधा:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 43.18015)
- **Original**: मधुकैटभौ महादैत्यौ लीलया ह्तुमुद्दतौ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 43.18016)
- **Original**: बोधयामास॒ गोविन्द विनाशहेतवे. तयो:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 43.18017)
- **Original**: सर्वेश्वरस्तवया सार्धमनीशो5यं_ त्वया बिना
- **Translation**: 

---

### Verse 7 (Vaivtpuran 43.18018)
- **Original**: त्वया अ् विष्णुना साध रक्षितो5ह सुरेश्वरि
- **Translation**: 

---

### Verse 8 (Vaivtpuran 43.18019)
- **Original**: स्वात्मदर्शनपुण्येन.. क्रीणीहि.. परमेश्वरि
- **Translation**: 

---

### Verse 9 (Vaivtpuran 43.18020)
- **Original**: इति श्रीब्रह्मवैवर्ते शिवेत कृत प्रकृत्या: स्तोत्र सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 43
- **Translation**: 

---

### Verse 10 (Vaivtpuran 43.18021)
- **Original**: 74--96) #3//- लिए 9090050 शिवकृतं दुर्गास्तोत्रम्‌ श्रोमहादेव उवाच रक्ष रक्ष महादेवि दुर्गे दुर्गतिनाशिनि । विष्णुमाये. महाभागे नारायेणि सनातनि । मां भक्तमनुरक्त च शत्रुग्रस्त॑ कृपामयि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 43.18022)
- **Original**: ख्रहास्वरूपे. परमे.. नित्यानन्दस्वरूपिणि
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.8308)
- **Original**: 388 *» संक्षिप्त ऋकककऋकऋकऋ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.8309)
- **Original**: अंक 6 ##ऋ###### कक 54464 ######## 544 %########%$5%क पार्वतीकी शिवसे प्रार्थना, परशुरामको देखकर उन्हें मारनेके लिये उद्यत होना, परशुरामद्वारा इृष्टदेवका ध्यान, भगवान्‌का वामनरूपसे पधारना, शिव-पार्वतीको समझाना और गणेशस्तोत्रको प्रकट करना पार्वतीने कहा--प्रभो! जगत्‌्में सभी लोग
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.8310)
- **Original**: जो कुछ कहा है, उसे क्षमा कौजिये। यदि आपने शंकरकी किंकरी मुझ दुर्गाको जानते हैं कि यह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.8311)
- **Original**: मेरा परित्याग कर दिया तो उस पुत्रसे क्या लाभ ? अपेक्षारहित दासी है, उसका जीवन व्यर्थ है। क्योंकि उत्तम कुलमें उत्पन्न हुई पतिब्रता नारीके परंतु ईश्वरके लिये तृणसे लेकर पर्व॑तपर्यन्त सभी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.8312)
- **Original**: लिये पति सौ पुत्रोंसे बढ़कर है। जो नारी नीच जातियाँ समान हैं; अतः दासीपुत्र गणेश और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 44.8313)
- **Original**: कुलमें उत्पन्न, दुष्टस्वभाववाली, ज्ञानीौन और आपके शिष्य परशुराम-इन दोनोंमें किसका दोष
- **Translation**: 

---

### Verse 18 (Vaivtpuran 44.8314)
- **Original**: माता-पिताके दोषसे निन्दित होती है, वह अपने है, इसपर विचार करना उचित है; क्योंकि आप
- **Translation**: 

---

### Verse 19 (Vaivtpuran 44.8315)
- **Original**: पतिको नहीं मानती। उत्तम कुलमें पैदा हुई स्त्री धर्मज्ञोमें श्रेष्ठ हैं। वीरभद्र, कार्तिकेय और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 44.8316)
- **Original**: अपने निन्दित, पतित, मूर्ख, दरिद्र, रोगी और पार्षदगण इसके साक्षी हैं। भला, गवाहीके काममें
- **Translation**: 

---

